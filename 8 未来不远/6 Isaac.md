遥操控制
```shell
sudo chmod 777 /dev/ttyACM0
cd ./Software/master_arm/
source install/setup.zsh
ros2 launch serial_bottom_driver double_master_serial.launch.py


ros2 run action_manager action_manager


ros2 run arm_executer arm_executer


ros2 service call /zmebot_trajectory_following dual_arm_interfaces/srv/TrajectoryFollowing "{trajectory_mode: 4}"

indices = [0, 3, 4, 5, 6, 7, 8, 9, 16, 12, 13, 14, 15, 11, 18, 20, 22, 24, 26, 28, 33, 34, 35, 36, 39, 40]

dof_pos_scaled[indices] = 0
```


```note
- rotate_base_joint
- lifting_base_joint
- gimbal_joint1
- left_joint1
- right_joint1
- gimbal_joint2
- left_joint2
- right_joint2
- left_joint3
- right_joint3
- left_joint4
- right_joint4
- left_joint5
- right_joint5
- left_joint6
- right_joint6
- left_joint7
- right_joint7
- left_finger_joint1
- left_finger_joint2
- ll_tool_joint3
- lr_tool_joint3
- right_finger_joint1
- right_finger_joint2
- rl_tool_joint3
- rr_tool_joint3
- lr_tool_joint2
- ll_tool_joint2
- rr_tool_joint2
- rl_tool_joint2




rotate_base_joint
lifting_base_joint
left_font_steering_joint1
left_rear_steering_joint3
left_whee_joint
right_font_steering_joint2
right_rear_steering_joint4
right_whee_joint
gimbal_joint1
left_joint1
right_joint1
left_font_drive_joint1
left_rear_drive_joint3
right_font_drive_joint2
right_rear_drive_joint4
gimbal_joint2
left_joint2
right_joint2
left_joint3
right_joint3
left_joint4
right_joint4
left_joint5
right_joint5
left_joint6
right_joint6
left_joint7
right_joint7
left_finger_joint1
left_finger_joint2
ll_tool_joint3
lr_tool_joint3
right_finger_joint1
right_finger_joint2
rl_tool_joint3
rr_tool_joint3
lr_tool_joint2
ll_tool_joint2
rr_tool_joint2
rl_tool_joint2
```

```shell
ros2 topic pub --once /isaac_joint_command sensor_msgs/JointState '{header: {stamp: {sec: 1720861606, nanosec: 489197117}, frame_id: ""}, name: ["right_joint1", "right_joint2", "right_joint3", "right_joint4", "right_joint5", "right_joint6", "right_joint7", "left_joint1", "left_joint2", "left_joint3", "left_joint4", "left_joint5", "left_joint6", "left_joint7", "left_finger_joint1", "left_finger_joint2", "right_finger_joint1", "right_finger_joint2"], position: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 1, 1]}'



ros2 topic pub --once /auto_joint_cmd dual_arm_interfaces/msg/AutonomyJointCommand "{left_joint_command: [{joint_position: 0.2},{joint_position: 0.2},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}],right_joint_command: [{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}]}"

ros2 topic echo /dual_arm_status | grep "gripper"


ros2 topic pub --once /dual_arm_status dual_arm_interfaces/msg/DualArmStatus "{
  left_arm_joints: [
    {joint_name: {data: "left_joint1"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint2"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint3"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint4"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint5"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint6"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "left_joint7"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4}
  ],
  right_arm_joints: [
    {joint_name: {data: "right_joint1"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint2"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint3"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint4"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint5"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint6"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4},
    {joint_name: {data: "right_joint7"}, joint_position: 0.0, joint_speed: 0.0, joint_current: 0.0, joint_torque: 0.0, joint_control: 0.0, joint_status: 4}
  ],
  left_arm_pose: {
    position: {x: 0.0, y: 0.0, z: 0.0},
    orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
  },
  right_arm_pose: {
    position: {x: 0.0, y: 0.0, z: 0.0},
    orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
  },
  left_gripper: {
    gripper_position: 0.0,
  },
  right_gripper: {
    gripper_position: 0.0,
  }
}"

```


```shell
ros2 run arm_executer arm_executer 
```


|               |     |
| ------------- | --- |
| base_link<br> | 200 |
| lifting       | 46  |
| left_wheel    | 100 |
| font_driver   | 10  |
| rear_driver   | 10  |


# 1 双臂
## 1.1 获取Isaac机器人姿态
**请求方式：Ros Topic**
**指令说明：上位机下发机器人关节，控制rviz机器人显示**
**话题名称：/isaac_joint_command**
**发布频率：信号触发**
**消息类型：sensor_msgs/JointState**
```topic
std_msgs/Header header
string[] name       # 关节名称列表
float64[] position  # 关节位置列表
float64[] velocity  # 关节速度列表
float64[] effort    # 关节力矩列表
```
**测试用例：**
```shell
ros2 topic pub /joint_command sensor_msgs/JointState '{header: {stamp: {sec: 1720861606, nanosec: 489197117}, frame_id: ""}, name: ["right_joint1", "right_joint2", "right_joint3", "right_joint4", "right_joint5", "right_joint6", "right_joint7", "left_joint1", "left_joint2", "left_joint3", "left_joint4", "left_joint5", "left_joint6", "left_joint7"], position: [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}'
```

## 1.2 下发Isaac机器人控制
**请求方式：Ros Topic**
**指令说明：上位机下发机器人关节，控制rviz机器人显示**
**话题名称：/isaac_joint_states**
**发布频率：信号触发**
**消息类型：sensor_msgs/JointState**
```topic
std_msgs/Header header
string[] name       # 关节名称列表
float64[] position  # 关节位置列表
float64[] velocity  # 关节速度列表
float64[] effort    # 关节力矩列表
```
**测试用例：**
```shell
ros2 topic pub /joint_command sensor_msgs/JointState '{header: {stamp: {sec: 1720861606, nanosec: 489197117}, frame_id: ""}, name: ["right_joint1", "right_joint2", "right_joint3", "right_joint4", "right_joint5", "right_joint6", "right_joint7", "left_joint1", "left_joint2", "left_joint3", "left_joint4", "left_joint5", "left_joint6", "left_joint7"], position: [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}'
```


```c++
      // try
      // {
      // }catch (const serial::IOException& e)
      // {
      //   PrintError(""); //If opening the serial port fails, an error message is printed //如果开启串口失败，打印错误信息
      // }catch (const std::exception& e) {
      //   std::string errorMessage = e.what();
      //   PrintError("Exception: " + errorMessage);
      // }
```

# 2 相机

**Isaac Utils > Common Omnigraphs > ROS2 Camera** (Window > Entensions > ROS2 bridge)
## 2.1 DCL(手)

|       | HFOV(16:9) | HFOV(4:3) |
| ----- | ---------- | --------- |
| rgb   | 86°        | 64°       |
| depth | 90°        |           |
| 红外    | 93°        |           |

设置必须符合DaBai DCL相机的规格  
SB3.0 :  
depth规格  
1280 x 800 @5/10/15/30 fps Y14/RLE  
640 x 400 @5/10/15/30/60[5] fps Y14/RLE  
320 x 200 @5/10/15/30/60[5] fps Y14/RLE  
color规格  
1920 x 1080 @5/10/15/30 fps MJPEG/YUYV  
1280 x 720 @5/10/15/30/60 fps MJPEG/YUYV  
640 x 480 @5/10/15/30/60 fps MJPEG/YUYV  
640 x 360 @5/10/15/30/60 fps MJPEG/YUYV
https://www.worldrobotconference.com/ex/product/414.html
## 2.2 DCW2(头)

|       | HFOV(16:9) | HFOV(4:3) |
| ----- | ---------- | --------- |
| rgb   | 86°        | 63°       |
| depth | 91°        |           |
| 红外    | 93°        |           |

https://www.orbbec.com.cn/index/Product/info.html?cate=38&id=55

![[Pasted image 20241203164759.png]]
# 3 动力学参数
真机：最大速度90°/s

![[动力学参数.png]]




