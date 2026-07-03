```shell
docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=Asia/Shanghai \
  -v /home/zme/Software/ha/config:/config \
  -v /run/dbus:/run/dbus:ro \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable
  
docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=Asia/Shanghai \
  -v /home/zme/Software/ha/config:/config \
  -v /run/dbus:/run/dbus:ro \
  --network=host \
  ghcr.nju.edu.cn/home-assistant/home-assistant:stable
  
docker run -d \
  --name hass-super \
  --restart=unless-stopped \
  --privileged \
  -e DEFAULT_TZ=Asia/Shanghai \
  -v /usr/share/hassio:/usr/share/hassio \
  -v /run/dbus:/run/dbus:ro \
  --device /dev/net/tun \
  --network=host \
  ghcr.nju.edu.cn/hasscc/hass-super
  
docker stop homeassistant
docker rm homeassistant

mkdir config/custom_components
unzip hacs.zip -d hacs
mv hacs config/custom_components
```

- `/PATH_TO_YOUR_CONFIG` 指向存储配置的文件夹，并运行容器。请确保保留 `:/config` 部分。
- D-Bus 是可选的，但如果您计划使用蓝牙集成，则必须启用。


