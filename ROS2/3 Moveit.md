
# 0 环境
```shell
sudo apt install  ros-$ROS_DISTRO-moveit ros-$ROS_DISTRO-moveit-setup-assistant -y

# 这个功能包用于管理控制器
sudo apt install ros-$ROS_DISTRO-controller-manager -y
# 两个控制器，一个关节轨迹控制器，另一个是关节状态发布器
sudo apt install ros-$ROS_DISTRO-joint-trajectory-controller ros-$ROS_DISTRO-joint-state-broadcaster -y


# https://control.ros.org/rolling/index.html
sudo apt-get install ros-$ROS_DISTRO-ros2-controllers
sudo apt-get install ros-$ROS_DISTRO-gazebo-ros2-control
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
# 2 Moveit编程

[https://blog.csdn.net/qq_43557907/article/details/125679824](https://blog.csdn.net/qq_43557907/article/details/125679824)
```shell
ros2 pkg create \
 --build-type ament_cmake \
 --dependencies moveit_ros_planning_interface rclcpp \
 --node-name hello_moveit hello_moveit
```

```cpp
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit_visual_tools/moveit_visual_tools.h>
#include <chrono>
#include <thread>

using namespace std::chrono_literals;


int main(int argc, char * argv[])
{
  // Initialize ROS and create the Node
  rclcpp::init(argc, argv);
  auto const node = std::make_shared<rclcpp::Node>(
    "hello_moveit",
    rclcpp::NodeOptions().automatically_declare_parameters_from_overrides(true)
  );


  // static const std::string PLANNING_GROUP = "l_arm";
  // moveit::planning_interface::MoveGroupInterface move_group(node, PLANNING_GROUP);
  // namespace rvt = rviz_visual_tools;
  // moveit_visual_tools::MoveItVisualTools visual_tools(node, "zmebot_left_arm_hand_tcp", "move_group", move_group.getRobotModel());
  // std::vector<geometry_msgs::msg::Pose> waypoints;
  // visual_tools.publishPath(waypoints, rvt::BLUE, 0.005);




  // Create a ROS logger
  auto const logger = rclcpp::get_logger("hello_moveit");
  std::cout << "hello" << std::endl;

  // Create the MoveIt MoveGroup Interface
  using moveit::planning_interface::MoveGroupInterface;
  auto move_group_interface = MoveGroupInterface(node, "l_arm");

  // 设置目标容差
  move_group_interface.setGoalJointTolerance(0.001);

  // 设置最大速度和加速度缩放因子
  move_group_interface.setMaxAccelerationScalingFactor(0.2);
  move_group_interface.setMaxVelocityScalingFactor(0.2);

  // 控制机械臂先回到初始化位置
  move_group_interface.setNamedTarget("l_center");
  move_group_interface.move();
  std::cout << "返回l_center" << std::endl;
  std::this_thread::sleep_for(1s);


  double target_pose[7] = {0.391410, -0.676384, -0.376217, 0.0, 1.052834, 0.454125, 0.3};
  std::vector<double> joint_group_positions(7);
  joint_group_positions[0] = target_pose[0];
  joint_group_positions[1] = target_pose[1];
  joint_group_positions[2] = target_pose[2];
  joint_group_positions[3] = target_pose[3];
  joint_group_positions[4] = target_pose[4];
  joint_group_positions[5] = target_pose[5];
  joint_group_positions[6] = target_pose[6];

  move_group_interface.setJointValueTarget(joint_group_positions);
  move_group_interface.move();
  std::cout << "到达目标" << std::endl;
  std::this_thread::sleep_for(1s);


  // 控制机械臂回到初始化位置
  move_group_interface.setNamedTarget("l_center");
  move_group_interface.move();
  std::cout << "返回l_center" << std::endl;
  std::this_thread::sleep_for(1s);


  // auto const target_pose2 = []{
  //   geometry_msgs::msg::Pose msg;
  //   msg.orientation.w = 1.0;
  //   msg.orientation.x = 0.0;
  //   msg.orientation.y = 0.0;
  //   msg.orientation.z = 0.0;
  //   msg.position.x = 0.28;
  //   msg.position.y = -0.2;
  //   msg.position.z = 0.5;
  //   return msg;
  // }();
  // move_group_interface.setPoseTarget(target_pose2);
  // move_group_interface.move();
  // std::cout << "到达目标" << std::endl;


  // Shutdown ROS
  rclcpp::shutdown();
  return 0;
}
```
# 3 调试
```shell
# 对应Plan轨迹
ros2 topic echo /display_planned_path
# 对应Execute轨迹
ros2 topic echo /l_arm_controller/follow_joint_trajectory/_action/feedback

# 对应Execute按钮
ros2 topic echo /execute_trajectory/_action/feedback
# 对应Plan和Plaun & Execute按钮，存储起始点和目标点
ros2 topic echo /motion_plan_request
# 对应Execute和Plan & Execute按钮
ros2 topic echo /execute_trajectory/_action/status
```