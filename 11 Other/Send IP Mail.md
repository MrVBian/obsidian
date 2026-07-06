# 部署开机自启
```shell
mkdir -p ~/.config/systemd/user
cd ~/.config/systemd/user
vim ~/.config/systemd/user/ip_monitor_startup.service
vim ~/.config/systemd/user/ip_monitor.py
```
**service**
```service
[Unit]
Description=IP Monitor Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/zme/.config/systemd/user/ip_monitor.py
WorkingDirectory=/home/zme/.config/systemd/user
Restart=always
RestartSec=20

[Install]
WantedBy=default.target
```
**常用指令**
```shell
systemctl --user daemon-reload
systemctl --user enable ip_monitor_startup.service 
systemctl --user start ip_monitor_startup.service

systemctl --user status ip_monitor_startup.service

systemctl --user stop ip_monitor_startup.service

systemctl --user restart ip_monitor_startup.service
```
# 监听IP脚本
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ================== 用户配置区域 ==================
# 检测周期（秒）
CHECK_INTERVAL = 60

# 邮件配置（必填）
SMTP_SERVER = 'smtp.qq.com'
SMTP_PORT = 465
SENDER_EMAIL = '544207374@qq.com'
SENDER_PASSWORD = 'otlklimnvcvxbfgb'   # 不是登录密码
RECEIVER_EMAIL = '544207374@qq.com'

# 邮件标题前缀（可自定义）
EMAIL_SUBJECT_PREFIX = '网卡IP变化通知'
# ===============================================

def prefix_to_netmask(prefix):
    """将CIDR前缀（如24）转为点分十进制掩码（如255.255.255.0）"""
    mask = (0xffffffff >> (32 - prefix)) << (32 - prefix)
    return f"{(mask >> 24) & 0xff}.{(mask >> 16) & 0xff}.{(mask >> 8) & 0xff}.{mask & 0xff}"

def get_physical_interfaces():
    """
    自动识别物理网卡：名称以 en, eth, wl, wlan 开头，
    并且排除 lo、docker、veth、br- 等虚拟设备。
    返回列表，如 ['enp3s0', 'wlp2s0']
    """
    try:
        # 列出 /sys/class/net/ 下的所有接口
        ifaces = os.listdir('/sys/class/net/')
    except FileNotFoundError:
        # 备用方法：使用 ip link 解析
        output = subprocess.check_output(['ip', '-o', 'link', 'show']).decode()
        ifaces = re.findall(r'\d+:\s+(\S+):', output)
    # 过滤：保留有线/无线常见前缀，排除虚拟设备
    physical = []
    for iface in ifaces:
        # 跳过 lo, docker*, veth*, br-*, virbr*, tap*, tun* 等
        if iface.startswith(('lo', 'docker', 'veth', 'br-', 'virbr', 'tap', 'tun')):
            continue
        # 保留 en*, eth*, wl*, wlan*
        if iface.startswith(('en', 'eth', 'wl', 'wlan')):
            physical.append(iface)
    return physical

def get_ip_and_mask(iface):
    """
    获取指定网卡的 IPv4 地址和子网掩码（点分十进制）
    返回 (ip, netmask) 或 (None, None)
    """
    try:
        output = subprocess.check_output(['ip', '-4', 'addr', 'show', iface], stderr=subprocess.DEVNULL)
        output = output.decode('utf-8')
        match = re.search(r'inet\s+(\d+\.\d+\.\d+\.\d+)/(\d+)', output)
        if not match:
            return None, None
        ip = match.group(1)
        prefix = int(match.group(2))
        netmask = prefix_to_netmask(prefix)
        return ip, netmask
    except Exception:
        return None, None

def get_current_status(interfaces):
    """获取所有指定接口的状态，返回 {iface: (ip, mask)}"""
    status = {}
    for iface in interfaces:
        ip, mask = get_ip_and_mask(iface)
        status[iface] = (ip, mask)
    return status

def format_status(status):
    """格式化为可读文本"""
    lines = []
    for iface, (ip, mask) in status.items():
        if ip and mask:
            lines.append(f"{iface}: IP={ip}, 掩码={mask}")
        else:
            lines.append(f"{iface}: 未获取到有效IP（可能未连接）")
    return "\n".join(lines)

def send_email(subject, body):
    """发送邮件（使用全局邮件配置）"""
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"邮件发送失败: {e}")
        return False

def main():
    # 自动识别网卡
    interfaces = get_physical_interfaces()
    if not interfaces:
        print("错误：未自动识别到任何有线/无线网卡，请手动检查。")
        return

    print(f"监控以下网卡: {', '.join(interfaces)}")
    print(f"检测周期: {CHECK_INTERVAL} 秒")
    print("按 Ctrl+C 停止")

    last_status = None

    while True:
        try:
            current = get_current_status(interfaces)

            # 判断是否变化：比较所有网卡的 (ip, mask)
            changed = False
            if last_status is None:
                changed = True  # 首次运行
            else:
                for iface in interfaces:
                    if last_status.get(iface) != current.get(iface):
                        changed = True
                        break

            if changed:
                # 构造邮件
                body = f"检测时间: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                body += format_status(current)
                subject = f"{EMAIL_SUBJECT_PREFIX} - {time.strftime('%H:%M:%S')}"
                print(f"[{time.strftime('%H:%M:%S')}] 状态变化，发送邮件...")
                success = send_email(subject, body)
                if success:
                    print("邮件发送成功")
                    last_status = current
                else:
                    print("邮件发送失败，下次继续尝试")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] 无变化，跳过")

            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\n脚本已手动退出")
            break
        except Exception as e:
            print(f"运行出错: {e}，等待 {CHECK_INTERVAL} 秒后重试...")
            time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    main()
```