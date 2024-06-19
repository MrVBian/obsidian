# 1 app open when system start

```shell
# 查找应用程序的.desktop
ll /usr/share/applications | grep appName
ln -s /usr/share/applications/utools.desktop ~/.config/autostart/
# 检查
ll $HOME/.config/autostart/ | grep utools
```
gnome-session-properties
![[Pasted image 20240530141253.png]]
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