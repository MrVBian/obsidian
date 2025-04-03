# 1 app open when system start

## 1.1 图形化操作增加指令
```shell
# 查找应用程序的.desktop
ll /usr/share/applications | grep appName
ln -s /usr/share/applications/utools.desktop ~/.config/autostart/
# 检查
ll $HOME/.config/autostart/ | grep utools
```
## 1.2 编辑启动程序
```shell
gnome-session-properties
```
![[Pasted image 20240530141253.png]]
## 1.3 开机脚本

确定Ubuntu系统使用的是哪种初始化系统：
```shell
ps -p 1 -o comm=
```
> 该命令将输出PID 1的进程的名称。如果输出是`systemd`，则系统使用的是`systemd`作为初始化系统。如果输出是`init`，则系统使用的是`SysV init`作为初始化系统。docker会输出bash，以上两种都不满足

### 1 `systemd`作为初始化系统

ROS开机自启脚本，创建脚本
```shell
vim start.sh
```
脚本内容：
```shell
#!/bin/bash

# 等待ROS 2核心服务启动
sleep 5

# 设置ROS 2工作空间
source /home/zme/zmebot_data_collection/install/setup.bash

# 执行你想要自启动的ROS 2节点
ros2 run data_collection listener
```
脚本运行权限，创建开机自启配置文件
```shell
chmod +x start.sh
sudo vim /etc/systemd/system/zmebot_data_collection_startup.service
```
开机自启配置文件内容(20s重连一次)：
```shell
[Unit]
Description=zmebot_data_collection Startup
After=network.target

[Service]
Environment="ROS_DOMAIN_ID=45"
User=zme
Group=zme
ExecStart=/home/zme/zmebot_data_collection/start.sh
WorkingDirectory=/home/zme/zmebot_data_collection
Restart=always
RestartSec=20

[Install]
WantedBy=default.target
```
启用开机自启动服务：
```shell
sudo systemctl daemon-reload
sudo systemctl enable zmebot_data_collection_startup.service
sudo systemctl status zmebot_data_collection_startup.service
```
日志
```shell
sudo journalctl -u zmebot_data_collection_startup.service
sudo journalctl -u zmebot_data_collection_startup.service -f
```
# 2 VMware

0 下载地址

https://softwareupdate.vmware.com/cds/vmw-desktop/ws/

1 赋予 .bundle 文件执行权限
```shell
sudo chmod +x VMware-Workstation-Full-16.0.0-16894299.x86_64.bundle
```
2 安装
```shell
sudo ./VMware-Workstation-Full-16.0.0-16894299.x86_64.bundle
```
3 卸载
```shell
sudo vmware-installer -u vmware-workstation
```
4 问题处理

4.1 VMware17.5.0激活码：MC60H-DWHD5-H80U9-6V85M-8280D

4.2 以下错误为内核不支持，更换VMare版本

![[Pasted image 20240523094919.png]]

4.3 windows10专业版激活

1.鼠标右击“开始”

2.选择Windows PowerShell（管理员）

输入slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX按回车键

第二行光标位置输入slmgr /skms [http://kms.03k.org](https://link.zhihu.com/?target=http%3A//kms.03k.org)按回车键

第三行光标位置输入slmgr /ato按回车键

# 3 安装uGet+Aria2，并接管Chorme下载

0 安装uGet
```shell
sudo add-apt-repository ppa:plushuang-tw/uget-stable
sudo apt-get update
sudo apt-get install uget
```
2 安装Aria2
```shell
sudo add-apt-repository ppa:t-tujikawa/ppa
sudo apt-get update
sudo apt-get install aria2
```
![[Pasted image 20240523115402.png]]

3 Chorme插件下载：[https://chrome.google.com/webstore/detail/uget-integration/efjgjleilhflffpbnkaofpmdnajdpepi?hl=zh-CN](https://chrome.google.com/webstore/detail/uget-integration/efjgjleilhflffpbnkaofpmdnajdpepi?hl=zh-CN)

```shell
sudo add-apt-repository ppa:uget-team/ppa
sudo apt update
sudo apt install uget-integrator
```

# 4 Ubuntu Editor to VCode in Unity

VCode插件：
1. C# by Microsoft
2. C# Dev Kit
3. Unity
4. Unity Code Snippets

https://code.visualstudio.com/docs/other/unity
https://www.youtube.com/watch?v=ywKFzU1jPsg

# 5 Halo

```shell
apt update
apt install -y nodejs npm
# 如果你没有 pug 以及 stylus 的渲染器，安装
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

# 6 Filezilla

```shell
sudo apt-get install filezilla
```
# 7 Blender

```shell
/opt/blender-4.1.1-linux-x64/4.1/python/bin/python3.11 -m pip install --upgrade pip
```

# 8 wechat

铜豌豆Linux优化后的原生版本
```shell
wget -c -O atzlinux-v12-archive-keyring_lastest_all.deb https://www.atzlinux.com/atzlinux/pool/main/a/atzlinux-archive-keyring/atzlinux-v12-archive-keyring_lastest_all.deb
sudo apt -y install ./atzlinux-v12-archive-keyring_lastest_all.deb
sudo apt update
sudo cp /etc/lsb-release /etc/lsb-release.Ubuntu
sudo apt -y install com.tencent.wechat
sudo apt -y install electronic-wechat-icons-atzlinux
sudo cp /etc/lsb-release /etc/lsb-release.wechat
```

# 9 ssh
```shell
sudo apt install openssh-server			# 安装ssh服务器
sudo apt install openssh-client			# 安装ssh客户机
sudo vim /etc/ssh/ssh_config

# 重启刷新配置
sudo /etc/init.d/ssh restart
```

# 10 obsidian

https://obsidian.md/download
https://github.com/MrVBian/obsidian

```shell
sudo vim /usr/share/applications/obsidian.desktop 
sudo cp obsidian.desktop ~/.local/share/applications/obsidian.desktop # add applications
```
设置->编辑->关闭拼写检查(Spellcheck)
```desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=obsidian
Exec="/home/zme/software/Obsidian-1.5.12.AppImage"
Icon=/home/zme/software/obsidian.svg
Terminal=false
Categories=navicat;
```
![[obsidian.svg]]
# 11 omniverse

```shell
sudo vim /usr/share/applications/omniverse.desktop 
```

```desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=omniverse
Exec="/home/zme/software/omniverse-launcher-linux.AppImage"
Icon=/home/zme/software/omniverse.png
Terminal=false
```
![[omniverse.png]]

# 12 磁盘
```shell
sudo apt install ncdu
sudo ncdu /var/log

# rm
sudo rm /var/log/syslog
```
# 13 Frp
下载：
```shell
wget https://github.com/fatedier/frp/releases/download/v0.61.2/frp_0.61.2_linux_amd64.tar.gz
tar -zxvf frp_0.61.2_linux_amd64.tar.gz
cd frp_0.61.2_linux_amd64/


sudo cp /path/to/your/frpc /usr/local/bin/
```
## 配置开机自启

```shell
cd /etc/systemd/system/
sudo vim frpc.service
```
service文件：
```service
[Unit]
Description=frpc
After=network.target
Wants=network.target

[Service]
Restart=on-failure
RestartSec=5
ExecStart=/home/username/Software/frp/frpc -c /home/username/Software/frp/frpc.ini

[Install]
WantedBy=multi-user.target
```
开机自启：
```shell
# 刷新服务列表
sudo systemctl daemon-reload
# 设置开机自启
sudo systemctl enable frpc.service
# 启动服务
sudo systemctl start frpc.service
```
## Server
```toml
bindPort = 10000

auth.method = "token"   #服务端连接身份认证，默认token
# 服务端token密码
auth.token = ""

# 允许监听的端口范围（供多个笔记本使用）
allowPorts = [
  { start = 10001, end = 10020 }
]
```

## Client
```toml
# frpc.toml
serverAddr = ""
serverPort = 10000
auth.token = ""

[[proxies]]
name = "ssh"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 10001

[[proxies]]
name = "mariadb"
type = "tcp"
localIP = "127.0.0.1"
localPort = 3306
remotePort = 10002

[[proxies]]
name = "oj_80"
type = "tcp"
localIP = "127.0.0.1"
localPort = 80
remotePort = 10010

[[proxies]]
name = "oj_443"
type = "tcp"
localIP = "127.0.0.1"
localPort = 443
remotePort = 10011
```
## Terminal
```shell
ssh -p 端口 内网服务器的用户名@公网服务器的IP
```

曲师大校园网Frp：
```
tkTdSxdFXxRkPVBvdJVUVv2cxpt7SeVUAvrDhsbEUXRMdYvMyNY3GU7tKmNC5B4G58mTEKGYR35NN2KBmF547UdxmH4sWCcB2HBfcw7DBkJ554FE5XkVyY75AH6QbtG7MZj4GwbJu5fMYNuVbSGETGyjvpuf7MJAYHpvWteEmp2QxG2Xjcy8PS7887EHF2Gx5AzRteCBdRVZV86YkS8sHpjnCdUkyy3Dt8X5fp6WhxePpmMsaU5p3hVHWzSDwtVf5d8Y4THxK833GHjXKw7zJZ2GQXK2csuxYtaxr8rNXwsH3ukM5QTVuMzhPKEc7jXC6bZD4RUuaR4H4BGeKwBcbku4vfhfcRdN8KyBnF2zQS3AVUbvasr6fbwPvHpNPDb7f7rdRGyDrV54wQByU2S8KVuVXnCYxHJ8fkucYfK7TfyeyS6rhzxJR6DvQFwZRZDKvf2VVxnWWF2RK58TSwHtCFdAK3sQaMnN4wRz5zpTTe268MH5cDckB5w63VN7zPEmhKMWnMTepjuNvP2NsfhZJhCD7y7tBKpWUE5A3HHfCXvj6SmyXw3vUbTWeWp3N6mGdceh6haFzF475Va5mF83Q2UWc2vXNmKjnEZsRDBfxkZ45GKYXw2tjStFE5n7e8mRtkJZvYJkQ3zXkw4Rnx3xjWrV4jFBwYT5pEtQfszBwQhUr2nfZ8C3R63RrZZ23VEcwVTukkGaacGxDzzdNUPZmZt47B3tGaTKfT8BXVxGDeKCX8PEtfFe3TFsh5YAA5QP8Te5QNtebHH8aVkb2NCASQtHzfY6tcxHTQUfHembKYMMshQJZdGWSTaftGyYbDYUCMZb8Vy5bVEfJWXXmWm4MVGPjSvDpRyRQRHGKhNMPvdQD78DsVt46S6t7DSsPRyxDQt2FAE8YBxmAJ5cUcSrWhtK7bcDT5xUk3WTWWcvFASAWm4HEUC3uF68xe5aGdMRbHvuYeEGek4TQnM57yXbH8x6WzjUzBQpEKDdyhBtnkC2U7eDRAFNGKwf4GDBPNZC
```