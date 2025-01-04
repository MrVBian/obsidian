
# 0 系统按键

| 内容      | 按键      |
| ------- | ------- |
| 主目录     | A-e     |
| 启动终端    | C-t     |
| 隐藏所有窗口  | A-d     |
| 切换全屏    | C-space |
| 在右侧查看分割 | A+右     |
| 在左侧查看分割 | A+左     |
| 恢复窗口    | A+下     |
| 最大化窗口   | A+上     |
## 环境变量
```shell
export TERMINAL="alacritty"
alias sudo='sudo '
alias nv='nvim'
alias na='nautilus . &'
alias raj='joshuto'
alias ra='ranger'
alias his='history'
alias ty='typora'
alias om='/home/zme/software/omniverse-launcher-linux.AppImage'
alias tm='tmux'
alias lg='lazygit'
alias blender='/opt/blender-4.1.1-linux-x64/blender'
alias py='python3'
alias python='python3'

alias cb='colcon build'
alias cbp='colcon build --packages-select'
alias sz='source ./install/setup.zsh'
# 启动通配符(*)
setopt nonomatch



alias po="export https_proxy=127.0.0.1:7890 && export http_proxy=127.0.0.1:7890 && export ftp_proxy=127.0.0.1:7890 && ALL_PROXY=127.0.0.1:7890"
alias pf="unset http_proxy https_proxy ftp_proxy ALL_PROXY"
 
# 指定X11服务器的UNIX域套接字文件的路径，通常在需要在X11环境中运行图形界面应用程序
XSOCK=/tmp/.X11-unix
# 允许所有用户访问X11服务
# xhost +
# xhost限制访问：限制可连接到X服务器的客户端。例如，可以使用以下命令只允许本地用户连接
# xhost +localhost
```
## gnome
[https://extensions.gnome.org/local/](https://extensions.gnome.org/local/)
```
 AppIndicator and KStatusNotifierItem Support  
 Audio Switcher  
 Auto Move Windows  
 Bluetooth Quick Connect  
 Clipboard Indicator  
 Coverflow Alt-Tab  
 Dash to Dock  
 Desktop Icons NG (DING)  
 Docker Integration  
 fluoroom's Top Bar  
 OpenWeather  
 Removable Drive Menu  
 Workspace Indicator
```
# 1 开发环境
![[wallhaven-9weyz8.jpg]]
https://github.com/MrVBian/config
https://github.com/MrVBian/nvim

拷贝.config下配置文件
- alacritty
- ranger
- tmux
拷贝~/下
- .tmux
- .tmux.conf
- .tmux-powerlinerc.default
- .oh-my-zsh
- .p10k.zsh
- .zshrc
## alacritty
```shell
sudo add-apt-repository ppa:aslatter/ppa
sudo apt update
sudo apt install alacritty
```
## neovim
> apt install 不是最新版本，不兼容lazyvim
```shell
# https://github.com/neovim/neovim/releases/tag/stable
tar xzvf nvim-linux64.tar.gz
rm -rf nvim-linux64.tar.gz
mkdir -p ~/.config/bin/
mv nvim-linux64 ~/.config/bin/nvim
cd /usr/bin
ln -s ~/.config/bin/nvim/bin/nvim nvim
```
### lazyvim
```shell
# https://www.lazyvim.org/installation
git clone https://github.com/LazyVim/starter ~/.config/nvim
rm -rf ~/.config/nvim/.git
```
## lazygit
```shell
LAZYGIT_VERSION=$(curl -s "https://api.github.com/repos/jesseduffield/lazygit/releases/latest" | \grep -Po '"tag_name": *"v\K[^"]*')
curl -Lo lazygit.tar.gz "https://github.com/jesseduffield/lazygit/releases/download/v${LAZYGIT_VERSION}/lazygit_${LAZYGIT_VERSION}_Linux_x86_64.tar.gz"
tar xf lazygit.tar.gz lazygit
sudo install lazygit -D -t /usr/local/bin/
```

## ranger
```shell
sudo apt-get install ranger
```
## tmux
```shell
sudo apt install tmux
# ~/.tmux.conf 修改设置默认为zsh
# set -g default-shell /bin/zsh
```
[rainbarf](https://github.com/creaktive/rainbarf/tree/v1.4)
```shell
sudo apt-get update
sudo apt-get install libmodule-build-perl
perl Build.PL
./Build test
sudo ./Build install
```

## zsh
https://blog.csdn.net/m0_72357534/article/details/135453423
安装后会自动加载配置文件
```shell
sudo apt install zsh
# 将zsh设置为默认shell
chsh -s /bin/zsh
```
### oh-my-zsh
```shell
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh

bash ./install.sh

# 命令行命令键入时的历史命令建议插件
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

- discord
- htop


[FiraCode Nerd Font字体](https://github.com/ryanoasis/nerd-fonts)
```shell
mv ./FiraCode /usr/share/fonts
```
![[Pasted image 20241017144254.png]]
# 2 软件
## Fzf
```shell
# 源码安装，需要网络
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install

# 升级
cd ~/.fzf && git pull && ./install
```
## UTools
https://u.tools/

## Snipaste
https://zh.snipaste.com/

## Clash Verge
https://github.com/zzzgydi/clash-verge/releases/
https://github.com/clash-verge-rev/clash-verge-rev/releases

## 钉钉
https://www.dingtalk.com/download#/

## ToDesk
https://www.todesk.com/

## VCode
https://code.visualstudio.com/
```
Isaac Sim VS Code Edition
docker

```

## Omniverse
```shell
./omniverse-launcher-linux.AppImage --proxy-server=127.0.0.1:7897
```

## WeChat
- https://flatpak.org/setup/
```shell
sudo apt install flatpak
```
