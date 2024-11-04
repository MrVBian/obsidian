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
[面板](http://172.30.24.201:3000/?orgId=1)