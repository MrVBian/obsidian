# 1 安装
## docker
```shell
curl -fsSL get.docker.com -o get-docker.sh
sudo sh get-docker.sh --mirror Aliyun
```
```shell
sudo apt update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
```
```shell
sudo groupadd docker               #添加用户组
sudo usermod -aG docker ${USER}    #将当前用户添加至用户组
newgrp docker                      #更新用户组
sudo service docker restart
```
## daemon
```shell
sudo tee /etc/docker/daemon.json <<-'EOF'
{
   "registry-mirrors": [
	 "https://hub-mirror.c.163.com",
	 "https://mirror.baidubce.com",
	 "https://docker.mirror.aliyuncs.com",
	 "https://reg-mirror.qiniu.com",
	 "https://docker.m.daocloud.io",
	 "https://mirror.ccs.tencentyun.com",
	 "https://registry.docker-cn.com",
	 "https://docker.mirrors.ustc.edu.cn",
	 "https://dockerproxy.com",
	 "https://mirror.aliyuncs.com",
	 "https://docker.nju.edu.cn",
	 "https://docker.1ms.run",
	 "https://docker.xuanyuan.me"
   ]
}
EOF
sudo systemctl daemon-reload && sudo systemctl restart docker
```
## compose
```shell
sudo curl -L "https://github.com/docker/compose/releases/download/v2.2.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

# 2 服务
## RustDesk-Server
```shell
vim docker-compose.yml
```
16行换成自己IP，16行和30行开启秘钥
秘钥在data路径下.pub文件
```yml
version: '3'

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:latest
    command: hbbs -r 172.24.3.132:21117 -k _
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:latest
    command: hbbr -k _
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

```shell
docker-compose up -d
```
![[Pasted image 20241224114659.png]]

```config
31 436 550
172.24.3.132
fcF1c5xyFQqIAevTd8lylQHLVR3tNtpFIbIc+5xGzS4=
```

# 3 软件