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