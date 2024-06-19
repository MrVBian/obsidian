
# 0 环境
```shell
sudo apt-get install ros-$ROS_DISTRO-moveit

# 这个功能包用于管理控制器
sudo apt install ros-$ROS_DISTRO-controller-manager -y
# 两个控制器，一个关节轨迹控制器，另一个是关节状态发布器
sudo apt install ros-humble-joint-trajectory-controller ros-humble-joint-state-broadcaster -y


# https://control.ros.org/rolling/index.html
sudo apt-get install ros-humble-ros2-controllers
sudo apt-get install ros-humble-gazebo-ros2-control
```
> [!error] 异常
> ```
> Action server: /recognize_objects not available
> MoveGroup namespace changed: / -> . Reloading params.
> ```
> 这个错误可以不处理

> [!error] 异常
> ```
> Could not find parameter robot_description_semantic and did not receive robot_description_semantic via std_msgs::msg::String subscription within 10.000000 seconds.
Error:   Could not parse the SRDF XML File. Error=XML_ERROR_EMPTY_DOCUMENT ErrorID=13 (0xd) Line number=0
at line 715 in ./src/model.cpp
Unable to parse SRDF
Robot model not loaded
> ```

把joint_limits.yaml中所有的valu改为浮点型，即0.0

![[Pasted image 20240613192611.png]]

# 1 使用
```shell
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```

