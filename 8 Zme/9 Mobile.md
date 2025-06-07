# 0 环境
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
-v "/home/zme/Software/mosquitto/config:/mosquitto/config" \
-v "/home/zme/Software/mosquitto/data:/mosquitto/data" \
-v "/home/zme/Software/mosquitto/log:/mosquitto/log" \
eclipse-mosquitto:2.0
```

```shell
sudo apt install libfmt-dev

sudo apt update
sudo apt install ros-$ROS_DISTRO-mqtt-client

# depend
sudo apt install ros-$ROS_DISTRO-ros-environment
colcon build --packages-up-to mqtt_client --cmake-args -DCMAKE_BUILD_TYPE=Release
```
调试
```shell
ros2 launch mqtt_client standalone.launch.ros2.xml

cd /opt/ros/humble/share/mqtt_client/config
vim params.ros2.yaml

ros2 topic pub /ros2mqtt std_msgs/msg/String "{data: \"Hello MQTT\"}"
```

方案2
```shell
pip install paho-mqtt
```
# 1 接口


## 6.1 机器人

### 6.1.1 机器人

**请求方式：MQTT**
**Topics：robot/robot/robot_id**（robot_id是变量）
**指令说明：桁架设备数采的数据通信接口**

```json
{
	"robots":[
		{
			"joint_state": [0.0, 0.0, 0.0, 0.0, -90.0, 0.0],
			"io_state": [0, 0, 0, 0, 0, 0, 0, 0], // 一个元素代表八个磁点。一个位对应一个磁点
			"servo_state": [5.0, 1.0]
		}
	]
}
```

| 参数        | 参数类型 | 说明                                                         | 实例值              |
| ----------- | -------- | ------------------------------------------------------------ | ------------------- |
| id          | string   | 单个臂的id                                                   | device1             |
| joint_state | float[]  | 可变长数组，通常为六关节                                     | [10,20,30,40,50,60] |
| io_state    | int[]    | 一个bit对应一个bool信号，预留八个byte(1byte=8bit)，共64个信号 | [0,0,0,0,0,0,0,0]   |
| servo_state | float[]  | 伺服数值的数组                                               | [5.0, 1.0]          |



### 6.1.2 桁架

**请求方式：MQTT**
**Topics：robot/truss/truss_id**（truss_id是变量）
**指令说明：桁架设备数采的数据通信接口**

```json
{
	"robots": [
		{
		    "id": "id1","joint_state": [0, 0, 0, 0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0],"servo_state": [0],
		    "attachment": {"parts group id": "", "part id": "", "rotation": 30.0}
		},
		{
		    "id": "id1","joint_state": [0, 0, 0, 0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0],"servo_state": [0],
		    "attachment": {"parts group id": "", "part id": "", "rotation": 30.0}
		}
	]
}
```

| 参数           | 参数类型 | 说明                                                         | 实例值              |
| -------------- | -------- | ------------------------------------------------------------ | ------------------- |
| id             | string   | 单个臂的id                                                   | device1             |
| joint_state    | float[]  | 预留六个关节的关节值，单位mm                                 | [10,20,30,40,50,60] |
| io_state       | int[]    | 一个bit对应一个bool信号，预留八个byte(1byte=8bit)，共64个信号 | [0,0,0,0,0,0,0,0]   |
| servo_state    | float[]  | 伺服数值的数组                                               | [5.0, 1.0]          |
| attachment     | object   | 当开磁后，桁架具体抓件的时刻才会有此字段，存在此字段时生成零件，无此字段时有零件则自由落体 | object              |
| parts group id | string   | 套料图Id                                                     | "M201009SG10008A07" |
| part id        | string   | 零件Id                                                       | "61#152#140_2"      |
| rotation       | float    | part_rotation，零件抓取姿态用角度，俯视图逆时针为正方向，用以区分同一零件不同抓取姿态，如下图所示 | 30.0f               |

![](./imgs/201.png)

## 6.2 制造设备

### 6.2.1 切割机

**请求方式：MQTT**
**Topics：manufacture/cutter/cutter_id**（cutter_id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    "robots": [
		{"id": "id1","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]},
		{"id": "id2","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]}
	]
}
```

| 参数          | 参数类型    | 说明                                          | 实例值                   |
| ----------- | ------- | ------------------------------------------- | --------------------- |
| id          | string  | 单个臂的id                                      | device1               |
| joint_state | float[] | 预留六个关节的关节值，单位mm                             | [1000,20,30,40,50,60] |
| io_state    | int[]   | 一个bit对应一个bool信号，预留八个byte(1byte=8bit)，共64个信号 | [0,0,0,0,0,0,0,0]     |

### 6.2.2 矫平机

**请求方式：MQTT**
**Topics：manufacture/leveler/leveler_id**（cutter_id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    state:1
}
```

| 参数  | 参数类型 | 说明                 | 实例值 |
| ----- | -------- | -------------------- | ------ |
| state | int      | 0：未启动<br>1：启动 | 1      |

### 6.2.3 喷码机

**请求方式：MQTT**
**Topics：manufacture/inkjet_printing/inkjet_printing_id**（inkjet_printing_id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    state:1
}
```

| 参数  | 参数类型 | 说明                            | 实例值 |
| ----- | -------- | ------------------------------- | ------ |
| state | int      | 0：未启动<br>1：启动<br>2：喷码 | 1      |

## 6.3 传送设备

### 6.3.1 程控行车

**请求方式：MQTT**
**Topics：conveyer/Program-controlled_driving/id**（id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    "data": [
		{"id": "id1","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]},
		{"id": "id2","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]}
	]
}
```

| 参数        | 参数类型 | 说明                                                         | 实例值              |
| ----------- | -------- | ------------------------------------------------------------ | ------------------- |
| id          | string   | 单个臂的id                                                   | device1             |
| joint_state | float[]  | 预留六个关节的关节值                                         | [10,20,30,40,50,60] |
| io_state    | int[]    | 一个bit对应一个bool信号，预留八个byte(1byte=8bit)，共64个信号 | [0,0,0,0,0,0,0,0]   |

### 6.3.2 KBK

**请求方式：MQTT**
**Topics：manufacture/kbk/kbk_id**（kbk_id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    "data": [
		{"id": "id1","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]},
		{"id": "id2","joint_state": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],"io_state": [0, 0, 0, 0, 0, 0, 0, 0]}
	]
}
```

| 参数        | 参数类型 | 说明                 | 实例值              |
| ----------- | -------- | -------------------- | ------------------- |
| id          | string   | 单个臂的id           | device1             |
| joint_state | float[]  | 预留六个关节的关节值 | [10,20,30,40,50,60] |