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
# 提升至root权限且修改rustdesk
```shell
# 停止并禁用原用户服务，避免重复运行
systemctl --user disable --now ip_monitor.service

# 创建由 root 运行的系统服务
sudo tee /etc/systemd/system/ip_monitor.service >/dev/null <<'EOF'
[Unit]
Description=IP Monitor Service
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
Group=root
Environment=RUSTDESK_USER=zme
Environment=PYTHONUNBUFFERED=1
ExecStart=/usr/bin/python3 /home/zme/.config/systemd/user/ip_monitor.py
WorkingDirectory=/home/zme/.config/systemd/user
Restart=always
RestartSec=20

[Install]
WantedBy=multi-user.target
EOF

# 重新加载、设置开机启动并启动服务
sudo systemctl daemon-reload
sudo systemctl enable ip_monitor.service
sudo systemctl restart ip_monitor.service
```
## 监听脚本
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
import sys
import copy
import ipaddress
import json
import shutil
import signal
import stat
import tempfile
from pathlib import Path

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
# RustDesk（Ubuntu 标准 deb 客户端 + 系统级 rustdesk.service）
RUSTDESK_ENABLED = True
# 多网卡建议填写，例如 'enp3s0'。留空时选默认路由网卡。
RUSTDESK_INTERFACE = 'enp4s0'
# 已根据目标 Ubuntu 的进程输出确认桌面用户为 zme，可用同名环境变量覆盖。
# 留空时自动识别 sudo 发起用户和正在运行 RustDesk 的用户。
RUSTDESK_USER = os.environ.get('RUSTDESK_USER', 'zme')
RUSTDESK_SERVICE = 'rustdesk.service'
# 留空使用 RustDesk 默认端口（ID 21116，中继 21117）。非默认端口填整数。
RUSTDESK_ID_PORT = 21116
RUSTDESK_RELAY_PORT = 21117
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

def _load_toml(text):
    try:
        import tomllib
    except ImportError:
        try:
            import toml as tomllib
        except ImportError as exc:
            raise RuntimeError(
                'Python 3.10 及以下请先安装：sudo apt install python3-toml'
            ) from exc
    return tomllib.loads(text)


def _server_addresses(ip):
    ip = str(ipaddress.IPv4Address(ip))
    addresses = []
    for port in (RUSTDESK_ID_PORT, RUSTDESK_RELAY_PORT):
        if port not in (None, ''):
            if not 1 <= int(port) <= 65535:
                raise ValueError('RustDesk 端口必须在 1～65535 之间')
            addresses.append('{}:{}'.format(ip, int(port)))
        else:
            addresses.append(ip)
    return tuple(addresses)


def select_rustdesk_ip(status):
    """指定网卡优先；否则选默认路由网卡，只有一个有效 IP 时作为备用。"""
    if RUSTDESK_INTERFACE:
        return status.get(RUSTDESK_INTERFACE, (None, None))[0]
    candidates = {name: values[0] for name, values in status.items()
                  if values[0] and not ipaddress.IPv4Address(values[0]).is_link_local}
    try:
        output = subprocess.check_output(
            ['ip', '-4', 'route', 'show', 'default'],
            stderr=subprocess.DEVNULL, timeout=10, universal_newlines=True)
        routes = []
        for line in output.splitlines():
            dev = re.search(r'\bdev\s+(\S+)', line)
            metric = re.search(r'\bmetric\s+(\d+)', line)
            if dev and dev.group(1) in candidates:
                routes.append((int(metric.group(1)) if metric else 0, dev.group(1)))
        if routes:
            return candidates[min(routes)[1]]
    except (OSError, subprocess.SubprocessError):
        pass
    if len(candidates) == 1:
        return next(iter(candidates.values()))
    if not candidates:
        return None
    raise RuntimeError('多个网卡有 IP，但无法确定默认网卡；请填写 RUSTDESK_INTERFACE')


def _updated_config(text, ip):
    """只修改三个地址字段，并解析校验，保留 Key/API/密码/其它配置及注释。"""
    id_server, relay_server = _server_addresses(ip)
    original = _load_toml(text)
    expected = copy.deepcopy(original)
    expected['rendezvous_server'] = id_server  # 同步 ID 服务器缓存
    options = expected.setdefault('options', {})
    if not isinstance(options, dict):
        raise ValueError('RustDesk2.toml 的 options 必须是 TOML 表')
    options['custom-rendezvous-server'] = id_server
    options['relay-server'] = relay_server
    if expected == original:
        return text

    pending = {
        '': {'rendezvous_server': id_server},
        'options': {'custom-rendezvous-server': id_server, 'relay-server': relay_server},
    }
    section = ''
    result = []
    seen_options = False

    def append_missing(name):
        values = pending.get(name, {})
        if values and result and not result[-1].endswith('\n'):
            result[-1] += '\n'
        for key, value in list(values.items()):
            result.append('{} = {}\n'.format(key, json.dumps(value)))
            del values[key]

    for line in text.splitlines(keepends=True):
        header = re.match(r'^\s*\[(.+?)\]\s*(?:#.*)?$', line)
        if header:
            append_missing(section)
            section = header.group(1).strip().strip('\"\'')
            seen_options |= section == 'options'
        else:
            assignment = re.match(r'^\s*([\w-]+|\"[^\"]+\"|\'[^\']+\')\s*=', line)
            if assignment:
                key = assignment.group(1).strip('\"\'')
                if key in pending.get(section, {}):
                    value = pending[section].pop(key)
                    line = '{} = {}\n'.format(key, json.dumps(value))
        result.append(line)
    append_missing(section)
    if not seen_options:
        if result and not result[-1].endswith('\n'):
            result[-1] += '\n'
        result.append('\n[options]\n')
        append_missing('options')
    updated = ''.join(result)
    if _load_toml(updated) != expected:
        raise ValueError('配置格式无法安全修改；已停止写入，请检查 RustDesk2.toml')
    return updated


def _run_systemctl(*args):
    result = subprocess.run(
        ['systemctl', *args, RUSTDESK_SERVICE],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True, timeout=45)
    if result.returncode:
        raise RuntimeError('systemctl {} {} 失败：{}'.format(
            ' '.join(args), RUSTDESK_SERVICE,
            (result.stderr or result.stdout).strip()))
    return result.stdout.strip()


def _rustdesk_processes():
    """读取实际进程及其用户/环境，避免用当前 sudo 的 HOME 推测配置目录。"""
    processes = []
    for entry in Path('/proc').iterdir():
        if not entry.name.isdigit():
            continue
        try:
            executable = os.readlink(str(entry / 'exe'))
            if Path(executable).name != 'rustdesk':
                continue
            args = (entry / 'cmdline').read_bytes().split(b'\0')
            args = [os.fsdecode(arg) for arg in args if arg]
            environment = {}
            for item in (entry / 'environ').read_bytes().split(b'\0'):
                if b'=' in item:
                    key, value = item.split(b'=', 1)
                    environment[os.fsdecode(key)] = os.fsdecode(value)
            # /proc/PID/stat 的第 22 项为进程启动时间，用来避免 PID 被复用后误杀。
            stat_fields = (entry / 'stat').read_text().rsplit(')', 1)[1].split()
            processes.append({
                'pid': int(entry.name), 'uid': entry.stat().st_uid,
                'start': stat_fields[19], 'exe': executable,
                'args': args[1:], 'env': environment,
            })
        except (FileNotFoundError, ProcessLookupError):
            continue
    return processes


def _config_targets(processes):
    import pwd  # Linux 模块，仅在 Ubuntu 上执行更新时导入
    targets = {}

    def add(user, env=None):
        env = env or {}
        base = env.get('XDG_CONFIG_HOME') or str(
            Path(env.get('HOME') or user.pw_dir) / '.config')
        if not Path(base).is_absolute():
            raise RuntimeError('XDG_CONFIG_HOME 必须是绝对路径')
        path = Path(base) / 'rustdesk' / 'RustDesk2.toml'
        targets[path] = user

    # 标准 deb 服务以 root 启动；桌面 --server 一般以登录用户启动。
    add(pwd.getpwuid(0))
    username = RUSTDESK_USER or os.environ.get('SUDO_USER', '')
    if username:
        add(pwd.getpwnam(username))
    for process in processes:
        add(pwd.getpwuid(process['uid']), process['env'])
    return targets


def _read_config(path):
    try:
        return path.read_text(encoding='utf-8-sig')
    except FileNotFoundError:
        return ''


def _write_config(path, text, user):
    """同目录原子替换，备份旧文件，并保留原文件属主和权限。"""
    missing = []
    parent = path.parent
    while not parent.exists():
        missing.append(parent)
        parent = parent.parent
    for directory in reversed(missing):
        directory.mkdir(mode=0o700)
        os.chown(str(directory), user.pw_uid, user.pw_gid)

    if path.exists():
        metadata = path.stat()
        backup = path.with_name(path.name + '.bak.' + str(time.time_ns()))
        shutil.copy2(str(path), str(backup))
        os.chown(str(backup), metadata.st_uid, metadata.st_gid)
        uid, gid, mode = metadata.st_uid, metadata.st_gid, stat.S_IMODE(metadata.st_mode)
    else:
        uid, gid, mode = user.pw_uid, user.pw_gid, 0o600
    descriptor, temporary = tempfile.mkstemp(prefix='.RustDesk2.', dir=str(path.parent))
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8', newline='\n') as output:
            os.fchown(output.fileno(), uid, gid)
            os.fchmod(output.fileno(), mode)
            output.write(text)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, str(path))
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _terminate_rustdesk():
    # 服务已停止；这里只处理仍持有旧配置的桌面窗口和残留子进程。
    for sig, wait_seconds in ((signal.SIGTERM, 8), (signal.SIGKILL, 3)):
        processes = _rustdesk_processes()
        for process in processes:
            try:
                fields = (Path('/proc') / str(process['pid']) / 'stat').read_text()
                if fields.rsplit(')', 1)[1].split()[19] == process['start']:
                    os.kill(process['pid'], sig)
            except (FileNotFoundError, ProcessLookupError):
                pass
        deadline = time.monotonic() + wait_seconds
        while time.monotonic() < deadline:
            if not _rustdesk_processes():
                return
            time.sleep(0.2)
    if _rustdesk_processes():
        raise RuntimeError('RustDesk 进程尚未完全退出，取消写入以防配置被覆盖')


def _restore_rustdesk_windows(processes):
    import pwd
    restored = set()
    for process in processes:
        # 仅恢复主窗口和托盘。--server 由服务管理，不重放连接/文件传输命令。
        if process['args'] not in ([], ['--tray']):
            continue
        env = process['env']
        if not (env.get('DISPLAY') or env.get('WAYLAND_DISPLAY')):
            continue
        identity = (process['uid'], tuple(process['args']))
        if identity in restored:
            continue
        restored.add(identity)
        if any(p['uid'] == process['uid'] and p['args'] == process['args']
               for p in _rustdesk_processes()):
            continue
        user = pwd.getpwuid(process['uid'])

        def drop_privileges(user=user):
            os.initgroups(user.pw_name, user.pw_gid)
            os.setgid(user.pw_gid)
            os.setuid(user.pw_uid)

        subprocess.Popen(
            [process['exe'], *process['args']], env=env, cwd=user.pw_dir,
            preexec_fn=drop_privileges, start_new_session=True,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def update_rustdesk(ip):
    """适用于 Ubuntu 上通过 deb 安装、由系统级 systemd 管理的标准 RustDesk。"""
    if not sys.platform.startswith('linux'):
        raise RuntimeError('RustDesk 更新仅在目标 Ubuntu 主机上运行')
    if os.geteuid() != 0:
        raise RuntimeError('更新 RustDesk 需要 root 权限，请用 sudo python3 ip_monitor.py 运行')
    if not shutil.which('systemctl'):
        raise RuntimeError('未找到 systemctl；本脚本要求系统级 rustdesk.service')
    if _run_systemctl('show', '--property=LoadState', '--value') != 'loaded':
        raise RuntimeError('未找到 RustDesk 系统服务，请确认已安装 deb 客户端')

    processes = _rustdesk_processes()
    targets = _config_targets(processes)
    # 写入前校验全部配置；格式错误或缺少 TOML 依赖时不停止 RustDesk。
    for path in targets:
        _updated_config(_read_config(path), ip)
    errors = []
    try:
        _run_systemctl('stop')
        _terminate_rustdesk()
        # 退出时配置可能刚刚落盘，因此退出后重新读取，不能使用退出前的快照。
        updates = [(path, user, _read_config(path)) for path, user in targets.items()]
        updates = [(path, user, old, _updated_config(old, ip))
                   for path, user, old in updates]
        for path, user, old, new in updates:
            if old != new:
                _write_config(path, new, user)
                print('RustDesk 配置已更新：{}'.format(path))
    except Exception as exc:
        errors.append(str(exc))
    finally:
        # 即使配置写入失败，也尽力恢复服务与原有主界面。
        try:
            _run_systemctl('start')
            time.sleep(3)
            _run_systemctl('is-active', '--quiet')
        except Exception as exc:
            errors.append('恢复 RustDesk 服务失败：{}'.format(exc))
        try:
            _restore_rustdesk_windows(processes)
        except Exception as exc:
            errors.append('恢复 RustDesk 界面失败：{}'.format(exc))
    if errors:
        raise RuntimeError('；'.join(errors))
    id_server, relay_server = _server_addresses(ip)
    for path in targets:
        options = _load_toml(_read_config(path)).get('options', {})
        # rendezvous_server 是运行期缓存，RustDesk 可能为它补上 :21116；
        # 验证用户设置中的两个地址，避免正常的缓存刷新触发重复重启。
        if (options.get('custom-rendezvous-server') != id_server
                or options.get('relay-server') != relay_server):
            raise RuntimeError('重启后服务器地址校验失败：{}'.format(path))
    return 'ID/中继服务器地址已更新为 {}，服务已启动且配置校验通过'.format(ip)


def process_status(current, interfaces, last_status, last_rustdesk_ip):
    """邮件与 RustDesk 各自记录成功状态，互不阻塞重试。"""
    rustdesk_result = 'RustDesk 自动更新未启用'
    if RUSTDESK_ENABLED:
        try:
            target_ip = select_rustdesk_ip(current)
            if not target_ip:
                rustdesk_result = '未获取到目标网卡有效 IP，暂不修改 RustDesk 配置'
            elif target_ip != last_rustdesk_ip:
                rustdesk_result = update_rustdesk(target_ip)
                last_rustdesk_ip = target_ip
            else:
                rustdesk_result = 'RustDesk 服务器 IP 无变化，无需重启'
        except Exception as exc:
            rustdesk_result = 'RustDesk 更新失败，下轮重试：{}'.format(exc)
        print(rustdesk_result)

    changed = last_status is None or any(
        last_status.get(iface) != current.get(iface) for iface in interfaces)
    if changed:
        body = '检测时间: {}\n\n'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
        body += format_status(current)
        body += '\n\n' + rustdesk_result
        subject = '{} - {}'.format(EMAIL_SUBJECT_PREFIX, time.strftime('%H:%M:%S'))
        print('[{}] 状态变化，发送邮件...'.format(time.strftime('%H:%M:%S')))
        if send_email(subject, body):
            print('邮件发送成功')
            last_status = current
        else:
            print('邮件发送失败，下次继续尝试')
    else:
        print('[{}] 无变化，跳过邮件'.format(time.strftime('%H:%M:%S')))
    return last_status, last_rustdesk_ip


def main():
    interfaces = get_physical_interfaces()
    if not interfaces:
        print("错误：未自动识别到任何有线/无线网卡，请手动检查。")
        return

    print(f"监控以下网卡: {', '.join(interfaces)}")
    print(f"检测周期: {CHECK_INTERVAL} 秒")
    print("RustDesk 目标网卡: " + (RUSTDESK_INTERFACE or "自动选择默认路由网卡"))
    print("按 Ctrl+C 停止")
    last_status = None
    last_rustdesk_ip = None

    while True:
        try:
            current = get_current_status(interfaces)
            last_status, last_rustdesk_ip = process_status(
                current, interfaces, last_status, last_rustdesk_ip)
            time.sleep(CHECK_INTERVAL)
        except KeyboardInterrupt:
            print("\n脚本已手动退出")
            break
        except Exception as exc:
            print(f"运行出错: {exc}，等待 {CHECK_INTERVAL} 秒后重试...")
            time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
```