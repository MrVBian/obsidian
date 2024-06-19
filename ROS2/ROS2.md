
# 0 基础配置

```shell
echo "\
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ focal-security main restricted universe multiverse">/etc/apt/sources.list

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

apt-get update
apt-get install vim -y
sudo apt install python-pip


sudo apt install ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-robot-state-publisher
```

# 1 ROS 基础指令
```shell
ros2 run <package> <execute>
ros2 node list
ros2 node info <nodeName>

# 功能包安装。安装自动放置到系统目录，不用再次手动source
# /opt/ros/humble/lib
# /opt/ros/humble/share
sudo apt insatll ros-<version>-packageName

# 列出可执行文件
# 列出所有
ros2 pkg executables
# 列出某个功能包
ros2 pkg executables turtlesim
# 列出所有包
ros2 pkg list
# 输出某个包所在路径前缀
ros2 pkg prefix <packageName>
# 列出包的清单描述文件
ros2 pkg xml <packageName>
```




## python
```shell
# colcon
sudo apt-get install python3-colcon-common-extensions

# 只编译一个包
colcon build --packages-select PKGName
# 允许更改src下部分文件改变install（重要）
colcon build --symlink-install
```



```
# 创建一个功能包
ros2 pkg create pkgName --build-type ament_python --dependencies rclpy
# build-type：ament_python、ament_cmake、cmake，缺省为ament_cmake


# python 安装依赖包
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
python3 -m pip3 install --upgrade pip
```

## cpp
```shell
# 创建一个功能包
ros2 pkg create pkgName --build-type ament_cmake --dependencies rclcpp

source /opt/ros/humble/setup.bash
```


# 2 interface
```shell
# 可以查看某一接口包下所有的接口
ros2 interface package pkgName
# 查看接口列表(当前环境下)
ros2 interface list
# 查看所有接口包
ros2 interface packages
# 查看某一个接口详细内容
ros2 interface show pkgName/msg/String
# 输出某一个接口所有属性
ros2 interface proto sensor_msgs/msg/Image



# 原始数据类型
bool
byte
char
float32, float64
int8,  uint8
int16, uint16
int32, uint32
int64, uint64
string
```


## Python
需要在CMakeLists.txt告诉编译器，把xx.msg转换为python和c++的头文件
```cmake
添加对sensor_.msgs的
find_package(sensor_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
# 添加消息文件和依赖
rosidl_generate_interfaces(${PROJECT_NAME}
  'msg/Novel.msg"
  DEPENDENCIES sensor_msgs
)
```

**修改package.xml**
```xml
<depend>sensor_msgs</depend>
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```

## C++

**CMakeLists.txt**

```cmake
find_package(xxInterface REQUIRED)

ament_target_dependencies(rclcpp
  xxInterface
)
```



# 3 通信
## 3.1 topic
```shell
# 查看话题信息
ros2 topic info topicName
# 返回系统中当前活动的所有主题列表,-t显示消息类型
ros2 topic list -t
# 打印实时话题内容
ros2 topic echo
# 查看话题频率
ros2 topic hz  topicName

# 可视化话题
rqt_graph
```

![[4.png]]

## 3.2 param

ROS支持的参数值类型：
- bool和bool[]
- int64和in64[]
- float64和float64[]
- string和string[]
- byte[]

```shell
# 查看节点有哪些参数
ros2 param list

# 查看一个参数的信息
ros2 param describe /turtlesim(node_name) background_b(param_name)

# 查看参数值
ros2 param get /turtlesim(node_name) background_b(param_name)

# 设置参数值
ros2 param get /turtlesim(node_name) background_b(param_name) 22(value)


# 保存参数值，生成一个yml文件
ros2 param dump /turtlesim(node_name)
# 恢复参数值
ros2 param load /turtlesim ./turtlesim.yml
# 启动时加载参数快照
ros2 run <pkg_name> <exe_name> --ros-args --params-file <file_name>

```

## 3.3 service

```shell
# 查看服务接口类型
ros2 service type /服务名
ros2 interface show 服务类型
# 查找使用某一接口的服务
ros2 service find 接口名

# python客户端
# https://www.bilibili.com/video/BV1gr4y1Q7j5?p=49&vd_source=4f10315acd30a6491a3fb1f267a3a517
# c++客户端
# https://www.bilibili.com/video/BV1gr4y1Q7j5?p=51&vd_source=4f10315acd30a6491a3fb1f267a3a517
```

## 3.4 action

## 3.5 ROS通信机制总结

- topic：单向、实时性高、频率高，实时性强的传感器数据一般用topic
- service：双向、频率较低，强调服务特性和反馈的场景一般用service
- param：用于配置节点，原理基于service
- action：实时反馈场景，原理基于topic和service
# 4 工具

## 4.1 launch

### 4.1.1 创建功能包和launch文件

创建文件夹和功能包，接着touch一个launch文件，后缀为`.py`。

```
mkdir -p chapt5/chapt5_ws/src
cd chapt5/chapt5_ws/src
ros2 pkg create robot_startup --build-type ament_cmake --destination-directory src
mkdir -p src/robot_startup/launch
touch src/robot_startup/launch/example_action.launch.py
```

### 4.1.2 启动多个节点的示例

需要导入两个库，一个叫做LaunchDescription，用于对launch文件内容进行描述，一个是Node，用于声明节点所在的位置。

> 注意这里要定一个名字叫做`generate_launch_description`的函数，ROS2会对该函数名字做识别。

```python
# 导入库
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    """launch内容描述函数，由ros2 launch 扫描调用"""
    action_robot_01 = Node(
        package="example_action_rclcpp",
        executable="action_robot_01"
    )
    action_control_01 = Node(
        package="example_action_rclcpp",
        executable="action_control_01"
    )
    # 创建LaunchDescription对象launch_description,用于描述launch文件
    launch_description = LaunchDescription(
        [action_robot_01, action_control_01])
    # 返回让ROS2根据launch描述执行节点
    return launch_description
```

### 4.1.3 将launch文件拷贝到安装目录

编写完成后直接编译会发现install目录下根本没有你编写的launch文件，后续launch自然也找不到这个launch文件。

因为用的是`ament_cmake`类型功能包，所以这里要使用cmake命令进行文件的拷贝
```cmake
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})
```
如果是`ament_python`功能包版
```python
from setuptools import setup
from glob import glob
import os

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    },
)
```
### 4.1.4 编译测试

使用colcon指令编译我们的程序
```shell
colcon build
```
编译完成后，在`chapt5/chapt5_ws/install/robot_startup/share/robot_startup/launch`目录下你应该就可以看到被cmake拷贝过去的launch文件了。
接着运行`
```shell
# source 第五章的工作目录，这样才能找到对应的节点，不信你可以不source试试
source ../../chapt5/chapt5_ws/install/setup.bash
source install/setup.bash
ros2 launch robot_startup example_action.launch.py
# 新终端
ros2 node list #即可看到两个节点
```
## 4.2 bag

https://zhuanlan.zhihu.com/p/694468853


# 调试
## 控制指令

```shell
ros2 topic pub /zmebot_joints_state sensor_msgs/msg/JointState "{name: [visual_zmebot_left_arm_joint_5,visual_zmebot_left_arm_joint_6],position: [2.1,-1.1]}"
ros2 launch zmebot_description display.launch.py use_drag:=0
ros2 launch zmebot_description display.launch.py use_drag:=0


ros2 run data_collection listener


ros2 topic pub /zmebot_joints_state sensor_msgs/msg/JointState "{name: [visual_zmebot_left_arm_joint_0,visual_zmebot_left_arm_joint_1,visual_zmebot_left_arm_joint_2,visual_zmebot_left_arm_joint_3,visual_zmebot_left_arm_joint_4,visual_zmebot_left_arm_joint_5,visual_zmebot_left_arm_joint_6],position: [30,30,30,30,30,30,30]}"

ros2 topic pub /zmebot_joints_state sensor_msgs/msg/JointState "{name: [visual_zmebot_left_arm_joint_0,visual_zmebot_left_arm_joint_1,visual_zmebot_left_arm_joint_2,visual_zmebot_left_arm_joint_3,visual_zmebot_left_arm_joint_4,visual_zmebot_left_arm_joint_5,visual_zmebot_left_arm_joint_6],position: [30,30,30,30,30,30,30]}"
```


## Error: joint_state_publisher_gui not found
```shell
sudo apt-get install ros-humble-joint-state-publisher-gui -y

# python 安装依赖包
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
python3 -m pip3 install --upgrade pip
pip3.10 install influxdb-client 
```


## zme第三方依赖

```shell
# 修改qpOASES工程的CMakelists.txt。OFF改为ON
# option(BUILD_SHARED_LIBS "If ON, build shared library instead of static" ON)
#!/bin/sh
# eigen must be 3.4 .
sudo apt-get -y install git cmake build-essential libboost-system-dev libboost-program-options-dev libboost-thread-dev libboost-test-dev pkg-config libeigen3-dev libboost-filesystem-dev

# URDF
sudo apt-get -y install liburdfdom-headers-dev liburdfdom-dev 

# hpp-fcl
git clone --branch v2.0.0  --recurse-submodules https://github.com/humanoid-path-planner/hpp-fcl.git
cd hpp-fcl
mkdir build && cd build
cmake .. -DBUILD_PYTHON_INTERFACE=OFF -DCMAKE_BUILD_TYPE=Release
make -j8 && sudo make install && cd ../..


# Pinocchio
git clone --branch v2.6.21 --recurse-submodules https://github.com/stack-of-tasks/pinocchio.git
cd pinocchio
mkdir build && cd build
cmake .. -DBUILD_PYTHON_INTERFACE=OFF -DBUILD_UNIT_TESTS=OFF -DBUILD_WITH_COLLISION_SUPPORT=ON -DCMAKE_BUILD_TYPE=Release
make -j8 && sudo make install && cd ../..


# qpOASES,change CMakeLists to generate .so .
git clone https://github.com/coin-or/qpOASES.git 
cd qpOASES
mkdir build && cd build
cmake .. && make -j8 && sudo make install && cd ../..

# qpSWIFT
git clone https://github.com/qpSWIFT/qpSWIFT.git
cd qpSWIFT
mkdir build && cd build
cmake .. 
make -j8 && sudo make install && cd ../.. 

# add to .bashrc
export PATH=/usr/local/bin:$PATH
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
export CMAKE_PREFIX_PATH=/usr/local:$CMAKE_PREFIX_PATH
```

需要依赖三个zme工程
```shell
source ../dependence/motion_control_interfaces/install/setup.bash
source ../dependence/ocs2_wbc/install/setup.bash
source ../dependence/glog-0.7.0/install/setup.bash
```
> [!error] qpOASES要编译动态库
> option(BUILD_SHARED_LIBS "If ON, build shared library instead of static" ON)


### 自己探索

```shell

git clone https://github.com/coin-or/qpOASES
cd qpOASES && mkdir build && cd build
cmake .. 
make
sudo make install 

git clone https://github.com/qpSWIFT/qpSWIFT
cd qpSWIFT && mkdir build && cd build
cmake .. 
make
sudo make install 


# https://stack-of-tasks.github.io/pinocchio/download.html
sudo apt install -qqy lsb-release curl
sudo mkdir -p /etc/apt/keyrings
 curl http://robotpkg.openrobots.org/packages/debian/robotpkg.asc \
     | sudo tee /etc/apt/keyrings/robotpkg.asc
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/robotpkg.asc] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg" \
     | sudo tee /etc/apt/sources.list.d/robotpkg.list
sudo apt update
sudo apt install -y robotpkg-py3*-pinocchio
```



## 测试指令：通信

```shell
docker exec -it ros /bin/bash
cd zmebot_hardware && source install/setup.bash


# 模式切换
ros2 service call /zmebot_trajectory_following motion_control_interfaces/srv/TrajectoryFollowing "{trajectory_mode: 2}"

# 自动关节
ros2 topic pub /auto_joint_control_cmd motion_control_interfaces/msg/AutonomyJointControl "{joints: [{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0},{joint_position: -0.6},{joint_position: 0.0},{joint_position: 0.0},{joint_position: 0.0}]}"

# 自动笛卡尔
ros2 topic pub /auto_cart_control_cmd motion_control_interfaces/msg/AutonomyCartesianControl "{pose: {position:{x: 0,y: -0.9,z: 0.5},orientation:{x: 0.64,y: 0.0,z: 0.0,w: 1.0}}}"

```

