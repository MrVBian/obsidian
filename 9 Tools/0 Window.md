# 1 Git SSH Agent
## 1.1 创建 PowerShell 配置文件
```powershell
# 如果文件不存在则自动创建
if (!(Test-Path $PROFILE)) { New-Item -Path $PROFILE -Type File -Force }
# 用记事本打开配置文件
notepad $PROFILE
code $PROFILE  # 如果已安装 VSCode
```
## 1.2 在配置文件中添加以下代码
```powershell
function Open-Proxy {
    $env:HTTP_PROXY = "http://127.0.0.1:7897"
    $env:HTTPS_PROXY = "http://127.0.0.1:7897"
    Write-Host "[OK] Proxy Enabled: 7897" -ForegroundColor Green
}

function Close-Proxy {
    $env:HTTP_PROXY = $null
    $env:HTTPS_PROXY = $null
    Write-Host "[OFF] Proxy Disabled" -ForegroundColor Red
}

Set-Alias po Open-Proxy
Set-Alias pf Close-Proxy
```
## 1.3 重新加载配置文件
```powershell
. $PROFILE
```