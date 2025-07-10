# 0 概述

**1号机Influxdb：**

| 服务           | 网址                           | 用户 : 密码             |
| ------------ | ---------------------------- | ------------------- |
| **InfluxDB** | http://192.168.152.165:8086/ | **admin:zme123456** |

**API Token：**

```tex
Esr-vlG-8WuLEqLaOkHgNKfFt_3ts6kIN3JiAgiwGX0u75W559JsldsF_uQSWxew5ZUoeB4qpPE313pKUOCJtQ==
```

**3号机Influxdb：**

| 服务         | 网址                         | 用户 : 密码         |
| ------------ | ---------------------------- | ------------------- |
| **InfluxDB** | http://192.168.152.166:8086/ | **admin:zme123456** |

**API Token：**

```tex
RjSeMIZW9VLqXb44TWggSWguNImzlV01XyFLQebJc5Le-HjuACjtCvH5OOVc7tVXKST2uXzqsP9G4kOPH_qPhw==
```

**7号机Influxdb：**

| 服务         | 网址                         | 用户 : 密码         |
| ------------ | ---------------------------- | ------------------- |
| **InfluxDB** | http://192.168.152.168:8086/ | **admin:zme123456** |

**API Token：**

```tex
I1BdLj3po_Ra4uKqE8t_bl3zrUYZuOg2TCQTBAA6KyCvss5GX4d8RBpevdcEowl88FfZdc8BRgNG81L5XF9Yfg==
```

**grafana：**

| 服务         | 网址                       | 用户 : 密码         |
| ------------ | -------------------------- | ------------------- |
| **InfluxDB** | http://172.30.24.201:3000/ | **admin:zme123456** |

# 1 用户手册

[打开面板](http://127.0.0.1:3000/d/bdld58hr6p9tsd/zmebot?orgId=1&refresh=5s)

# 2 配置Gafana

## 2.1 部署grafana
```shell
curl -fsSL https://test.docker.com -o test-docker.sh
sudo sh test-docker.sh
docker pull grafana/grafana
```

```shell
docker run -d --name grafana --net host grafana/grafana

# 可选参数，保存grafana配置项、插件、图表等
# -v yourpath:/var/lib/grafana
```

| 服务         | 网址                          | 用户 : 密码             |
| ---------- | --------------------------- | ------------------- |
| **Gafana** | http://127.0.0.1:3000/login | **admin:zme123456** |
## 2.2 获取Influxdb token
![[Pasted image 20240929163213.png]]
## 2.3 连接Influxdb

>  home -> Connections -> influxdb -> add new data source

其中password填入`2.1 获取Influxdb token`的token

![[Pasted image 20240929163256.png]]
![[Pasted image 20240929163316.png]]

在第二步中选择，import dashboard

```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 2,
  "links": [],
  "panels": [
    {
      "datasource": {
        "type": "influxdb",
        "uid": "adlca5prj8irkf"
      },
      "description": "关节速度",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 5,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "smooth",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "always",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": false,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "velocityms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 0
      },
      "id": 1,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hoverProximity": 1111,
          "maxHeight": -1,
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "adlca5prj8irkf"
          },
          "query": "from(bucket: \"ros\")\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n  |> filter(fn: (r) => r[\"_measurement\"] == \"SlaveArmStatus\")\n  |> filter(fn: (r) => r[\"_field\"] == \"joint_speed\")\n  |> filter(fn: (r) => r[\"joint_name\"] == \"link7\" or r[\"joint_name\"] == \"link6\" or r[\"joint_name\"] == \"link5\" or r[\"joint_name\"] == \"link4\" or r[\"joint_name\"] == \"link3\" or r[\"joint_name\"] == \"link2\" or r[\"joint_name\"] == \"link1\")\n  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\n  |> yield(name: \"mean\")",
          "refId": "A"
        }
      ],
      "title": "关节速度",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "influxdb",
        "uid": "adlca5prj8irkf"
      },
      "description": "关节力矩",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 5,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "smooth",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "always",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": false,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "forceNm"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 0
      },
      "id": 3,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hoverProximity": 1111,
          "maxHeight": -1,
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "adlca5prj8irkf"
          },
          "query": "from(bucket: \"ros\")\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n  |> filter(fn: (r) => r[\"_measurement\"] == \"SlaveArmStatus\")\n  |> filter(fn: (r) => r[\"_field\"] == \"joint_torque\")\n  |> filter(fn: (r) => r[\"joint_name\"] == \"link7\" or r[\"joint_name\"] == \"link6\" or r[\"joint_name\"] == \"link5\" or r[\"joint_name\"] == \"link4\" or r[\"joint_name\"] == \"link3\" or r[\"joint_name\"] == \"link2\" or r[\"joint_name\"] == \"link1\")\n  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\n  |> yield(name: \"mean\")",
          "refId": "A"
        }
      ],
      "title": "关节力矩",
      "transparent": true,
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "influxdb",
        "uid": "adlca5prj8irkf"
      },
      "description": "关节角度",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisBorderShow": false,
            "axisCenteredZero": false,
            "axisColorMode": "text",
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 5,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "insertNulls": false,
            "lineInterpolation": "smooth",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "always",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "fieldMinMax": false,
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "degree"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 8
      },
      "id": 2,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull"
          ],
          "displayMode": "table",
          "placement": "right",
          "showLegend": true
        },
        "tooltip": {
          "hoverProximity": 1111,
          "maxHeight": -1,
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "influxdb",
            "uid": "adlca5prj8irkf"
          },
          "query": "from(bucket: \"ros\")\n  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)\n  |> filter(fn: (r) => r[\"_measurement\"] == \"SlaveArmStatus\")\n  |> filter(fn: (r) => r[\"_field\"] == \"joint_position\")\n  |> filter(fn: (r) => r[\"joint_name\"] == \"link7\" or r[\"joint_name\"] == \"link6\" or r[\"joint_name\"] == \"link5\" or r[\"joint_name\"] == \"link4\" or r[\"joint_name\"] == \"link3\" or r[\"joint_name\"] == \"link2\" or r[\"joint_name\"] == \"link1\")\n  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)\n  |> yield(name: \"mean\")",
          "refId": "A"
        }
      ],
      "title": "关节角度",
      "transparent": true,
      "type": "timeseries"
    }
  ],
  "refresh": "5s",
  "schemaVersion": 39,
  "tags": [],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-5m",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "browser",
  "title": "zmebot",
  "uid": "bdld58hr6p9tsd",
  "version": 6,
  "weekStart": ""
}
```
# 3 配置Influxdb

![[Pasted image 20240929163335.png]]
# 4 测试

服务：

```shell
sudo systemctl restart zmebot_data_collection_startup.service
sudo systemctl status zmebot_data_collection_startup.service
```

日志：

```shell
sudo journalctl -u zmebot_data_collection_startup.service
sudo journalctl -u zmebot_data_collection_startup.service -f
```

topic检查：

```shell
ros2 topic list | grep slave_arm_status
ros2 topic echo /slave_arm_status
```

