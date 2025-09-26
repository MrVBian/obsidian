## Frp
/opt/frp

## drawDB
```shell
docker pull hub.rat.dev/xinsodev/drawdb  ##加上代理hub.rat.dev
docker run -d --name drawdb --restart always -p 3316:80 hub.rat.dev/xinsodev/drawdb
```
# minio

```shell
docker run -p 9000:9000 -p 9090:9090 \
     --name minio \
     -d --restart=always \
     -e "MINIO_ACCESS_KEY=admin" \
     -e "MINIO_SECRET_KEY=QfnU1024." \
     -v /home/qfnu/bzw/minio/data:/data \
     -v /home/qfnu/bzw/minio/config:/root/.minio \
     minio/minio:RELEASE.2023-04-28T18-11-17Z server \
     /data --console-address ":9090" -address ":9000"
```

