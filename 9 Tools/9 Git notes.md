- feat：新功能
- fix：修复Bug
- docs：文档
- style：格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
- test：添加测试或者修改现有测试
- chore：不修改src或者test的其余修改，例如构建过程或辅助工具的变动

丢弃本地所有修改
```shell
git reset --hard HEAD && git clean -df
```
完全丢弃最近的 commit
```shell
git reset --hard HEAD~1
```
恢复文件夹
```shell
git checkout HEAD -- path/to/folder/
```
**完全丢弃本地所有修改，强制同步远程最新版本**
```shell
# 1. 重置所有已修改的文件（丢弃所有未提交的更改）
git reset --hard HEAD

# 2. 彻底清理所有未跟踪的文件/目录（包括插件和.meta文件）
git clean -fd

# 3. 从远程仓库获取最新版本
git fetch origin

# 4. 强制将本地分支重置到和远程一致
git reset --hard origin/main
```

基于当前分支创建并切换到新的 `feat/test` 分支
```shell
git checkout -b feat/test
git add 
git commit -m "fix:"

git push --set-upstream origin feat/test
```

## 用户名和邮箱
### 查看
```shell
git config user.name
git config user.email
```
### 修改
```shell
git config user.name "zhenwei.bian"
git config user.email "zhenwei.bian@zhangmen.com"

git config user.name "MrVBian"
git config user.email "544207374@qq.com"

# 全局修改
git config --global user.name "MrVBian"
git config --global user.email "544207374@qq.com"
```
# Git SSH Agent
## 1 Window

```config
ProxyCommand connect -S 127.0.0.1:7897 -a none %h %p

Host github.com
  User git
  Port 22
  Hostname github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\zhenwei.bian\.ssh\id_rsa"
  TCPKeepAlive yes

Host ssh.github.com
  User git
  Port 443
  Hostname ssh.github.com
  # 注意修改路径为你的路径
  IdentityFile "C:\Users\zhenwei.bian\.ssh\id_rsa"
  TCPKeepAlive yes
```

## 2 Ubuntu

安装 `connect-proxy` 工具
```shell
sudo apt update && sudo apt install connect-proxy
```

```config
Host GitHub.com
  User git
  Port 22
  Hostname github.com
  IdentityFile "/home/bian/.ssh/id_rsa"
  # Linux/Mac:
  Proxycommand /usr/bin/ncat --proxy 127.0.0.1:7897 --proxy-type socks5 %h %p
```