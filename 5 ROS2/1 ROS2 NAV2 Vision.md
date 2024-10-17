# 1 环境

CycloneDDS是**一款基于DDS（Data Distribution Service）标准的实时通信中间件**，广泛应用于航空、航天、军事等领域。 CycloneDDS具有高效、可靠和灵活的特点，能够支持大规模分布式系统的实时通信需求。
```shell
sudo apt-get install ros-humble-rmw-cyclonedds-cpp
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
```

```shell
sudo apt-get install ros-humble-turtlebot3-gazebo
sudo apt-get install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*

export TURTLEBOT3_MODEL=waffle
```

```shell
sudo apt install ros-humble-slam-toolbox
```


真实激光雷达驱动
https://articulatedrobotics.xyz/tutorials/mobile-robot/hardware/lidar/
```shell
sudo apt install ros-humble-rplidar-ros
```
# 2 应用 


> [!warning] 地图加载报错
> 修改/opt/ros/humble/share/turtlebot3_navigation2/param/waffle.yaml
> robot_model_type: "nav2_amcl::DifferentialMotionModel"

```shell
# 窗口1
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

```shell
# 窗口2
ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True
```

```shell
# 窗口3
ros2 launch slam_toolbox online_async_launch.py use_sim_time=True
```

```shell
# 窗口4
ros2 run rviz2 rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz
```

```shell
# 窗口5
ros2 run turtlebot3_teleop teleop_keyboard
```


```shell
# 保存地图
ros2 run nav2_map_server map_saver_cli -f my_map
```