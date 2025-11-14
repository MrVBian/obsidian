目录结构如下：

- ui_splash_screen.h
- 

# Debug调试语句
```shell
# 查看当前topic
ros2 topic list

# 查看topic当前数据
ros2 topic echo /robot_pose_2d

# 查看topic类型
ros2 topic type /robot_pose_2d

# 管道过滤
ros2 topic list | grep robot
```
# 映射表

| Topic                   | package           | 注解      |             | 人员  |
| ----------------------- | ----------------- | ------- | ----------- | --- |
| /chassis_motor_feedback | serial_interfaces | 底盘的升降   |             | 王威博 |
| /robot_pose_2d          | []                | 底盘的位置   | [x, y]、底盘旋转 | 李斌  |
| /arm_status             | arm_interfaces    | 机械臂+机械手 | 关节角度(弧度)    | 诸铭瀚 |
| /robot_battery          | []                | 机器人电量   | 电量          |     |
| /gimble_steer_feedback  | serial_interfaces | 头/云台    |             |     |

# 机器人上的路径
```shell
cd /home/zme/robot/system/zme_robot/install/share
```
# 更新部署
- [ ] ROS2-TCP Server
```shell
cd /home/zme/TeleClient/ROS-TCP-Endpoint
colcon build
```
- [ ] Unity
	- [ ] 转C#代码，基于Ubuntu，ROS2