# 0 环境

```shell
uname -m
# 输出x86_64，则AMD
# 输出armv7l 或 arm 开头的其他值，则ARM
```

# 1 安装

```sh
# Ubuntu/Debian AMD64
curl -LO https://download.influxdata.com/influxdb/releases/influxdb2_2.7.6-1_amd64.deb
sudo dpkg -i influxdb2_2.7.6-1_amd64.deb
```

```shell
# Ubuntu/Debian ARM64
curl -LO https://download.influxdata.com/influxdb/releases/influxdb2_2.7.6-1_arm64.deb
sudo dpkg -i influxdb2_2.7.6-1_arm64.deb
```

# 2 启动服务

```shell
sudo service influxdb start
```

# 3 检查服务

```shell
sudo service influxdb status
```

如果成功，输出为以下：

```text
● influxdb.service - InfluxDB is an open-source, distributed, time series database
   Loaded: loaded (/lib/systemd/system/influxdb.service; enabled; vendor preset: enable>
   Active: active (running)
```

# 4 卸载服务

```shell
sudo apt remove influxdb2
sudo apt autoclean && sudo apt autoremove
```

# 5 重置账号

```shell
sudo rm /var/lib/influxdb/influxd.bolt
```

# 6 初始化密码和数据库

## 6.1 部署Influx CLI

```shell
# Ubuntu/Debian AMD64
wget https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.6.1-linux-amd64.tar.gz
tar xf influxdb2-client-2.6.1-linux-amd64.tar.gz 
cp influxdb2-client-2.6.1-linux-amd64/influx /usr/local/bin/

# Ubuntu/Debian ARM64
wget https://dl.influxdata.com/influxdb/releases/influxdb2-client-2.6.1-linux-arm64.tar.gz
tar xf influxdb2-client-2.6.1-linux-arm64.tar.gz 
cp influxdb2-client-2.6.1-linux-arm64/influx /usr/local/bin/
```

## 6.2 初始化密码和数据库

```shell
influx setup --org="zme" --bucket="ros" --username="admin" --password="zme123456" --token="I1BdLj3po_Ra4uKqE8t_bl3zrUYZuOg2TCQTBAA6KyCvss5GX4d8RBpevdcEowl88FfZdc8BRgNG81L5XF9Yfg==" --retention=360m --force
```

```text
I1BdLj3po_Ra4uKqE8t_bl3zrUYZuOg2TCQTBAA6KyCvss5GX4d8RBpevdcEowl88FfZdc8BRgNG81L5XF9Yfg==
```
[面板](http://172.30.24.201:3000/?orgId=1)


| 机器  | uid            |
| --- | -------------- |
| 11  | af4l6tlq6gikgd |
| 12  | cf4nd6u4sqz28b |
| 13  | ff4nohgshcglce |
| 14  | ff4negssjcsu8d |
| 15  | af4nej556f1moc |
| 33  | ff4nmbi0q7rb4e |


## 6.3 卸载

```shell
sudo systemctl stop influxdb.service 
sudo dpkg -r influxdb2
sudo rm -rf /var/lib/influxdb
sudo rm -rf /etc/influxdb


sudo dpkg -i influxdb2_2.7.6-1_amd64.deb
sudo systemctl stop influxdb.service 
```

## 6.4 初始化脚本

DBInit.sh
```shell
#!/bin/bash

# InfluxDB 2 初始化脚本（修复保留策略问题）
INFLUX_HOST="http://127.0.0.1:8086"

# 配置参数
ORG_NAME="zme"
BUCKET_NAME="ros"
ADMIN_USER="admin"
ADMIN_PASSWORD="zme123456"
API_TOKEN="I1BdLj3po_Ra4uKqE8t_bl3zrUYZuOg2TCQTBAA6KyCvss5GX4d8RBpevdcEowl88FfZdc8BRgNG81L5XF9Yfg=="
RETENTION_DURATION="72h" # 关键修复：使用持续时间字符串而非数字

# 服务检查函数
check_service() {
  if curl -s -v "$INFLUX_HOST/ping" 2>&1 | grep -q "204 No Content"; then
    echo "✅ InfluxDB服务可用"
    return 0
  fi
  return 1
}

# 主服务检查
if check_service; then
  echo "开始初始化InfluxDB..."
  echo "--------------------------------------------"
  echo "组织名称: $ORG_NAME"
  echo "存储桶: $BUCKET_NAME"
  echo "用户名: $ADMIN_USER"
  echo "保留周期: $RETENTION_DURATION"

  # 调用设置API（使用持续时间字符串）
  echo "发送初始化请求到: $INFLUX_HOST/api/v2/setup"
  response=$(
    curl -s -o response.json -w "%{http_code}" \
      -X POST "$INFLUX_HOST/api/v2/setup" \
      -H "Content-Type: application/json" \
      -d @- <<EOF
{
  "username": "$ADMIN_USER",
  "password": "$ADMIN_PASSWORD",
  "org": "$ORG_NAME",
  "bucket": "$BUCKET_NAME",
  "token": "$API_TOKEN",
  "retentionPeriod": "$RETENTION_DURATION"
}
EOF
  )

  # 处理响应
  echo "收到响应状态: $response"
  case $response in
  201)
    echo "--------------------------------------------"
    echo "✅ 初始化成功！"
    echo "--------------------------------------------"
    echo "访问地址: $INFLUX_HOST"
    echo "用户名: $ADMIN_USER"
    echo "密码: $ADMIN_PASSWORD"
    echo "API Token: $API_TOKEN"
    ;;
  409)
    echo "--------------------------------------------"
    echo "⚠️ 系统已经初始化过 (HTTP 409)"
    ;;
  *)
    echo "--------------------------------------------"
    echo "❌ 初始化失败 (HTTP $response)"
    echo "错误详情:"
    [ -f response.json ] && cat response.json || echo "无额外错误信息"
    exit 1
    ;;
  esac

  rm -f response.json
else
  echo "❌ 无法连接到InfluxDB服务"
  echo "请手动检查服务状态：curl -I $INFLUX_HOST/ping"
  exit 1
fi
```

# 7 开机自启服务
```shell
cd /home/zme/robot/teleocontrol/arm_project

# sudo vim /etc/systemd/system/zmebot_data_collection_startup.service
mkdir -p ~/.config/systemd/user
vim ~/.config/systemd/user/zmebot_data_collection_startup.service
```
Service：
```service
[Unit]
Description=zmebot_data_collection Startup
After=network.target

[Service]
# User=zme
# Group=zme
# ExecStart=/home/zme/robot/teleocontrol/arm_project/data_collect/start.sh
ExecStart=/bin/bash -lc '/home/zme/robot/teleocontrol/arm_project/data_collect/start.sh'
WorkingDirectory=/home/zme/robot/teleocontrol/arm_project/data_collect
Restart=always
RestartSec=20

[Install]
WantedBy=default.target
```
启动
```shell
cd data_collect
colcon build

sudo chmod +x start.sh

sudo systemctl daemon-reload
sudo systemctl enable zmebot_data_collection_startup.service
sudo systemctl restart zmebot_data_collection_startup.service
sudo systemctl status zmebot_data_collection_startup.service

sudo systemctl stop zmebot_data_collection_startup.service

chmod +x start.sh
systemctl --user daemon-reload
systemctl --user enable zmebot_data_collection_startup.service 
systemctl --user start zmebot_data_collection_startup.service
systemctl --user status zmebot_data_collection_startup.service


systemctl --user stop zmebot_data_collection_startup.service
```