https://zhuanlan.zhihu.com/p/21436538835
# 1 DeepSeek
### 1、安装 Ollama

ubuntu中可以在命令行中直接执行（国内网络安装比较慢）：
```shell
curl -fsSL https://ollama.com/install.sh | sh
```
输出ollama的版本号：
```shell
ollama -v
```

```shell
sudo systemctl able ollama
sudo systemctl disable ollama
sudo systemctl stop ollama
```
安装脚本会将 Ollama 设置为一个开机自动启动的服务，并通过 systemd 服务管理工具来确保它在系统启动时运行，且在异常退出时自动重启。
### 2、 部署DeepSeek推理模型

根据实际的环境配置，选择合适的 DeepSeek 尺寸模型进行部署。初次安装或者显卡资源少推荐先安装 1.5B或7B尺寸的模型。初次安装或者显卡资源少推荐先安装 1.5B或7B尺寸的模型。
```shell
ollama run deepseek-r1:32b
```
### 3、部署Dify
```shell
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d 
```
Dify 默认使用 80 端口，点击链接 `http://127.0.0.1` 即可访问
### 4、将DeepSeek模型接入Dify
点击 Dify 平台右上角**头像 → 设置 → 模型供应商**，选择 Ollama，点“添加模型”：
![[Pasted image 20250214111621.png]]
添加配置信息：  
1. Model Name，填写具体部署的模型型号。上文部署的模型型号为 deepseek-r1:32b，因此填写 `deepseek-r1:32b` 
2. Base URL，填写 Ollama 客户端的运行地址，通常为 `http://your_ollama_server_ip:11434`  
3. 其它选项可以保持默认值或按实际需要填