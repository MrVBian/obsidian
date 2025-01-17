
https://nodejs.org/zh-cn/download
https://golang.google.cn/doc/install
```
# 换源
npm config set registry https://registry.npmmirror.com

# vue ui
npm i -g @vue/cli

npm run dev -- --host 0.0.0.0 --port 5173
```

```shell
# 安装
go get github.com/gin-gonic/gin

# 更新
go get -u github.com/gin-gonic/gin

# 清理无效下载需要依赖
go mod tidy
```

# 1 Vue
```shell
# 安装依赖
npm install

# 启动开发环境
npm run dev

# 打包生产环境
npm run build

# 格式化或检查代码
npm run lint
```

## windows vscode 终端执行指令
1 打开 PowerShell 以管理员身份运行
2 **查看当前的执行策略：** 输入以下命令，查看当前的执行策略：
```powershell
Get-ExecutionPolicy
```
3 **更改执行策略：** 如果返回结果是 `Restricted` 或其他禁止脚本执行的策略，你可以更改为 `RemoteSigned` 或 `Unrestricted`，允许执行本地脚本。执行以下命令来更改策略：
```powershell
Set-ExecutionPolicy RemoteSignn  ed -Scope CurrentUser
```
4 重新启动 VSCode 或 PowerShell

## vscode插件
- Vue - Official
- Vue 3 Snippets
- 别名路径跳转