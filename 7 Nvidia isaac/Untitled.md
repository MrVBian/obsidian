### Isaac Sim Version

4.0.0

### Operating System

Ubuntu 22.04

## Topic Description

### Detailed Description

How to use OmniGraph Node for custom complex ROS msg format.

For example, I have a package called my_interfaces, which contains the following two msgs, MyJointState.msg and Joint.msg

The content of MyJointState.msg is as follows:
```ROSMsg
my_interfaces/Joint[7] left_arm_joints
geometry_msgs/Pose left_arm_pose
```

The content of msg and Joint.msg is as follows:
```ROSMsg
float32 joint_position
float32 joint_speed
float32 joint_current
float32 joint_torque
float32 joint_control
```

When I tried to follow the documentation([ROS 2 Generic Publisher and Subscriber](https://docs.omniverse.nvidia.com/isaacsim/latest/ros2_tutorials/tutorial_ros2_generic_publisher_subscriber.html#getting-started)), I found that:
- The left_arm_joints in MyJointState.msg cannot be displayed properly because it depends on Joint.msg
- The left_arm_pose in MyJointState.msg is displayed normally because it is a common field in ROS.

Special note: the above is an example to help you understand my problem, that is, there is a complex msg with A nested in B. The actual situation is more complicated than this.
How can I solve the above problem? Thank you for your reply!


我希望在nvidia isaac中模拟一款真实相机。真实相机工作距离为[0.2m,5m]，FOV：H86° V55° D93.5°。我在isaac相机中找到的属性有：Focal Length、Focus Distance、fStop、Horizontal Aperture、Vertical Aperture。请问我该如何配置isaac仿真中的相机属性，才能尽可能模拟真实相机


真实相机具体参数如下：

| 参数名称   | 数值         |
| ------ | ---------- |
| H FOV  | 86°        |
| V FOV  | 55°        |
| D FOV  | 93.5°      |
| 分辨率比例  | 16:9       |
| 传感器对角线 | **28.2mm** |
| 传感器比例  | 16:9       |

求水平光圈尺寸、垂直光圈尺寸、focal length和focus distance。请给出最终结果，保留两位小数


多相机视图，帧率很低。
当我只有一个视图时，帧率在60hz，当我启动四个视图时，帧率为13.7hz，但是主机的性能并没有发挥完，在CPU、GPU和内存上依然有较大冗余。
问题：
1、这是什么原因？
2、有什么优化方法？


### Isaac Sim Version
4.2.0
### Operating System
Ubuntu 22.04


Multiple camera views, low frame rate.
When I only have one view, the frame rate is 60hz, and when I start four views, the frame rate is 13.7hz, but the host's performance is not fully utilized, and there is still a large redundancy in CPU, GPU and memory.
Question:
1. What is the reason?
2. What are the optimization methods?