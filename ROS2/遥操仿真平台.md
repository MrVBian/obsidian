Github地址：[tiago_simulation](https://github.com/pal-robotics/tiago_simulation)

![[Pasted image 20240613164000.png]]

# 1 环境配置
```shell
echo "\
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse">/etc/apt/sources.list
apt-get update
apt-get install vim -y
mkdir -p ~/.config/pip
echo "\
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
">~/.config/pip/pip.conf
echo "\
source /opt/ros/humble/setup.bash
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
" >> ~/.bashrc
source ~/.bashrc


sudo apt-get install git python3-vcstool python3-rosdep python3-colcon-common-extensions
sudo apt install python3-pip
pip3 install setuptools==58.2.0
sudo apt install ros-humble-tiago-simulation
```



> [!warning] 注意事项
> 1、新版本setuptools：easy_install command is deprecated. Use build and pip and other standards-based tools.
> 	需要降低版本才能正常编译launch_pal包：pip3.10 install setuptools==58.2.0
> 2、[ERROR] [launch]: Caught exception in launch (see debug for traceback): "package 'pal_nav2_bringup' not found
> sudo apt install ros-humble-tiago-simulation
> # cd src/tiago_navigation
> git pull https://github.com/pal-robotics/tiago_navigation
> cd ../../


```shell
# Source the environment and build
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source ./install/setup.bash
ros2 launch tiago_gazebo tiago_gazebo.launch.py moveit:=False navigation:=True is_public_sim:=True world_name:=pal_office


# Gazebo仿真:
ros2 launch tiago_gazebo tiago_gazebo.launch.py is_public_sim:=True [arm:=no-arm]

# Launch gazebo simulation using PAL office gazebo world by executing:
ros2 launch tiago_gazebo tiago_gazebo.launch.py is_public_sim:=True world_name:=pal_office [arm:=no-arm]

# 移动机器人
# move the robot you can use the following command from another terminal
ros2 topic pub /mobile_base_controller/cmd_vel_unstamped geometry_msgs/msg/Twist '{linear: {x: 1}, angular: {z: 0}}' -r10

# Navigation
# You can launch TIAGo navigation by executing
ros2 launch tiago_2dnav tiago_nav_bringup.launch.py is_public_sim:=True

# Simulation + Navigation 2
# You can also start the simulation and navigation together by using
ros2 launch tiago_gazebo tiago_gazebo.launch.py navigation:=True is_public_sim:=True [arm:=no-arm]

ros2 launch tiago_gazebo tiago_gazebo.launch.py moveit:=False navigation:=True is_public_sim:=True world_name:=pal_office
```


```shell
sudo nv src/tiago_simulation/tiago_gazebo/launch/tiago_gazebo.launch.py
sim_nav -> nav


ros2 launch pmb2_gazebo pmb2_gazebo.launch.py is_public_sim:=True navigation:=True slam:=True
```