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

# Jenkins

```shell
sudo mkdir -p /opt/jenkins/jenkins_home
sudo mkdir -p /opt/jenkins/logs
sudo mkdir -p /opt/jenkins/docker
sudo chmod 777 /opt/jenkins



# 0b4cb832a6ef4f4f8ece2fb578cca93c
docker run -p 10008:8080 -p 10009:5000 --name jenkins \
--restart=always -u root \
-v /opt/jenkins/jenkins_home:/var/jenkins_home \
-v /opt/jenkins/logs:/var/logs \
-v /opt/jenkins/docker:/var/docker \
-v /var/run/docker.sock:/var/run/docker.sock \
-d jenkins/jenkins:lts

docker exec -it jenkins /bin/bash
cat /var/jenkins_home/secrets/initialAdminPassword
```