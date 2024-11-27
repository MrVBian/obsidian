```note
Joint 0 name: base_joint
Joint 1 name: rotate_base_joint
Joint 2 name: lifting_base_joint
Joint 3 name: gimbal_joint1
Joint 4 name: left_joint1
Joint 5 name: right_joint1
Joint 6 name: gimbal_joint2
Joint 7 name: left_joint2
Joint 8 name: right_joint2
Joint 9 name: gimbal_camera_joint
Joint 10 name: left_joint3
Joint 11 name: right_joint3
Joint 12 name: left_joint4
Joint 13 name: right_joint4
Joint 14 name: left_joint5
Joint 15 name: right_joint5
Joint 16 name: left_joint6
Joint 17 name: right_joint6
Joint 18 name: left_joint7
Joint 19 name: right_joint7
Joint 20 name: left_camera_base_joint
Joint 21 name: right_camera_base_joint
Joint 22 name: left_camera_joint
Joint 23 name: left_tool_base_joint
Joint 24 name: right_camera_joint
Joint 25 name: right_tool_base_joint
Joint 26 name: left_base_tool_joint
Joint 27 name: right_base_tool_joint
Joint 28 name: left_finger_joint1
Joint 29 name: left_finger_joint2
Joint 30 name: ll_tool_joint3
Joint 31 name: lr_tool_joint3
Joint 32 name: right_finger_joint1
Joint 33 name: right_finger_joint2
Joint 34 name: rl_tool_joint3
Joint 35 name: rr_tool_joint3
Joint 36 name: lr_tool_joint2
Joint 37 name: ll_tool_joint2
Joint 38 name: rr_tool_joint2
Joint 39 name: rl_tool_joint2



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
```

```shell
ros2 topic pub --once /isaac_joint_command sensor_msgs/JointState '{header: {stamp: {sec: 1720861606, nanosec: 489197117}, frame_id: ""}, name: ["right_joint1", "right_joint2", "right_joint3", "right_joint4", "right_joint5", "right_joint6", "right_joint7", "left_joint1", "left_joint2", "left_joint3", "left_joint4", "left_joint5", "left_joint6", "left_joint7", "left_finger_joint1", "left_finger_joint2", "right_finger_joint1", "right_finger_joint2"], position: [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 0]}'



ros2 topic pub --once /auto_joint_cmd dual_arm_interfaces/msg/AutonomyJointCommand "{left_joint_command: [{joint_position: 0.2},{joint_position: 0.2},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}],right_joint_command: [{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}]}"

```
```shell
ros2 run arm_executer arm_executer 
```

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

## 2.1 DCL(手)

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

https://www.orbbec.com.cn/index/Product/info.html?cate=38&id=55

# 3 动力学参数
![[动力学参数.png]]