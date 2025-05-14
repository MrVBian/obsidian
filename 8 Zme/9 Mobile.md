
```shell
docker pull eclipse-mosquitto:2.0


# 创建文件夹
mkdir mosquitto
# 进入mosquitto文件夹
cd mosquitto
 
# 创建配置文件夹、日志文件夹
mkdir config
mkdir data
mkdir log

docker run -itd --name mosquitto \
-p 1883:1883 -p 9001:9001 \
-v "$PWD/mosquitto/config:/mosquitto/config" \
-v "$PWD/mosquitto/data:/mosquitto/data" \
-v "$PWD/mosquitto/log:/mosquitto/log" \
eclipse-mosquitto:2.0
```