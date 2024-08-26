# 2 ROS接口
## 2.1 连接机器人
**请求方式：Ros Service**
**指令说明：上位机下发连接方式，并尝试连接机器人**
**话题名称：/zmebot_trajectory_following**
**消息类型：motion_control_interfaces/srv/TrajectoryFollowing**
```service
uint8 trajectory_mode

uint8 AUTONOMY_CARTESIAN = 0
uint8 AUTONOMY_JOINT = 1
uint8 TELEOPERATION_CARTESIAN = 2
uint8 TELEOPERATION_JOINT=3
uint8 IDLE=4
---
bool result
```

| 参数                                      | 参数类型  | 说明            | 实例值 |
| --------------------------------------- | ----- | ------------- | --- |
| trajectory_mode                         | uint8 | 轨迹模式，范围[0, 4] | 0   |
| AUTONOMY_CARTESIAN                      | uint8 | 自动笛卡尔模式       | 0   |
| AUTONOMY_JOINT                          | uint8 | 自动关节          | 1   |
| TELEOPERATION_CARTESIAN                 | uint8 | 遥操笛卡尔         | 2   |
| TELEOPERATION_JOINT                     | uint8 | 遥操关节          | 3   |
| IDLE                                    | uint8 | 空闲            | 4   |
| <font color="#ff0000">SIMULATION</font> | uint8 | 仿真模式          | 5   |
**测试用例：**
```shell
ros2 service call /zmebot_trajectory_following motion_control_interfaces/srv/TrajectoryFollowing "{trajectory_mode: 1}"
```
## 2.2 底盘控制
**请求方式：Ros Action**
**指令说明：底盘位姿目标**
**话题名称：/base_transform_status**
**消息类型：**
```action
builtin_interfaces/Time stamp
geometry_msgs/Pose target_pose
---
bool result
---
builtin_interfaces/Time current_stamp
geometry_msgs/Pose current_pose
bool aborted
bool finished
```
## 2.3 底盘同步
**请求方式：Ros Topic**
**指令说明：底盘位姿信息**
**话题名称：/base_transform_status**
**发布频率：20Hz**
**消息类型：**
```topic
builtin_interfaces/Time stamp
geometry_msgs/Pose current_pose
```
## 2.4 关节控制
**请求方式：Ros Topic**
**指令说明：上位机下发机器人关节，控制机器人**
**话题名称：/auto_joint_control_cmd**
**发布频率：20Hz**
**消息类型：motion_control_interfaces/msg/AutonomyJointControl**
```topic
motion_control_interfaces/Header header
motion_control_interfaces/Joint[7] joints
	motion_control_interfaces/String joint_name
	#  radius ,radius/s , A,N*m .
	float32 joint_position
	float32 joint_speed
	float32 joint_current
	float32 joint_torque
	# TODO more details , in joint pos control mode ,every joint_stauts will be 4 .
	uint8 joint_status

uint8 gripper_cmd

uint8 GRASPING = 1
uint8 RELEASING = 2
uint8 IDLE = 0
```
**测试用例：**
```shell
# 自动关节
ros2 topic pub /auto_joint_control_cmd motion_control_interfaces/msg/AutonomyJointControl "{joints: [{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: -0.6},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}]}"
```
## 2.5 笛卡尔坐标控制
**请求方式：Ros Topic**
**指令说明：上位机下发机器人笛卡尔坐标，控制机器人**
**话题名称：/auto_cart_control_cmd**
**发布频率：20Hz**
**消息类型：motion_control_interfaces/msg/AutonomyCartesianControl**
```topic
motion_control_interfaces/Header header
geometry_msgs/Pose pose

uint8 gripper_cmd

uint8 GRASPING = 1
uint8 RELEASING = 2
uint8 IDLE = 0
```
**测试用例：**
```shell
ros2 topic pub /auto_cart_control_cmd motion_control_interfaces/msg/AutonomyCartesianControl "{pose: {position:{x: 0,y: -0.9,z: 0.5},orientation:{x: 0.64,y: 0.0,z: 0.0,w: 1.0}}}"
```
## 2.6 关节-笛卡尔同步
**请求方式：Ros Topic**
**指令说明：机器人发布关节、笛卡尔数据**
**话题名称：/slave_arm_status**
**发布频率：20Hz**
**消息类型：motion_control_interfaces/msg/SlaveArmStatus**
```topic
motion_control_interfaces/Header header
motion_control_interfaces/Joint[8] joints
geometry_msgs/Pose current_pose

# currently ,if any joint status is not 4,error_code is 1,and manipulator will not be controlled .
uint32 error_code

# vibrate level
uint8 vibrate

# five defferent modes,refer to srv/TrajectoryFollowing.
uint8 trajectory_following_mode

# if it is 1,means an external controller is controlling manipullator,any commands from orin will not be executed .
uint8 external_controller_running

# TODO more details .
uint8 msg_type
uint8 SLAVE_MSG_TYPE = 1
```
**测试用例：**
```shell
ros2 topic pub /auto_joint_control_cmd motion_control_interfaces/msg/AutonomyJointControl "{joints: [{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: -0.6},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}]}"
```
## 2.7 上电-抱闸-速度状态
**请求方式：Ros topic**
**指令说明：机器人发布上电、抱闸状态和关节速度**
**话题名称：/robot_status**
**发布频率：5s**
**消息类型：**
```topic
builtin_interfaces/Time stamp # 时间戳
string[16] names   # 名称
bool[16] power_on  # 上电状态。true上电;false断电
bool[16] brake     # 抱闸状态。true抱闸;false未抱闸
float32[16] speed  # 速度。单位rad/s
```
## 2.8 关节上电请求
**请求方式：Ros service**
**指令说明：关节{name}上电请求**
**消息类型：**
```service
string name
bool power_on_checking
bool power_on = true
bool power_off = false
---
bool result
```
## 2.9 电池电量
**请求方式：Ros Topic**
**指令说明：机器人发布电池电量**
**话题名称：/robot_battery**
**发布频率：1min**
**消息类型：**
```service
builtin_interfaces/Time stamp # 时间戳
uint8 battery  # 范围[0, 100]
```