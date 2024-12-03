
# 0 依赖

```shell
sudo apt-get install ros-$ROS_DISTRO-xacro
sudo apt-get install ros-$ROS_DISTRO-urdf
```

# 1 查看编辑

## 1.1 jupyterlab

> [!NOTE] URDF查看和编辑器
> https://jupyterlab-urdf.readthedocs.io/en/latest/use_viewer.html

```shell
pip install jupyterlab
pip install notebook
pip install jupyterlab-urdf
# jupyterlab启动插件
```

## 1.2 ros-urdf

```shell
sudo apt-get install ros-$ROS_DISTRO-urdf-tutorial
ros2 launch urdf_tutorial display.launch.py model:=/home/zme/my_robot.urdf
```

# 2 URDF工具

在 ROS 中，提供了一些工具来方便 URDF 文件的编写，比如:

- `check_urdf`命令可以检查复杂的 urdf 文件是否存在语法问题
- `urdf_to_graphiz`命令可以查看 urdf 模型结构，显示不同 link 的层级关系

当然，要使用工具之前，首先需要安装，安装命令:`sudo apt install liburdfdom-tools`

## 2.1 check_urdf 语法检查

进入urdf文件所属目录，调用：
```shell
check_urdf xxx.urd
```
如果不抛出异常，说明文件合法,否则非法

## 2.2 urdf_to_graphiz 结构查看

进入urdf文件所属目录，调用：
```shell
urdf_to_graphiz xxx.urdf
```
当前目录下会生成 pdf 文件
![[Pasted image 20240604184518.png]]
# 3 urdf xacro sdf互转

**xacro 转 urdf**
```shell
xacro model.xacro > model.urdf
ros2 run xacro xacro my_robot.xacro > my_robot.urdf
```

**urdf 转 xacro**
```shell
ros2 run xacro xacro zmebot.urdf -o zmebot.xacro
```

**urdf转sdf**
```shell
gz sdf -p my_model.urdf > my_model.sdf
```

# 4 matlab urdf
![[URDF]]

---
# 未归纳


```
sudo apt-get install ros-$ROS_DISTRO-joint-state-publisher-gui ros-$ROS_DISTRO-robot-state-publisher
```


```shell
# Topic控制
ros2 launch zmebot_description display.launch.py use_drag:=0

# UI 控制
ros2 launch zmebot_description display.launch.py use_drag:=1
```



package://
package://zmebot_description/urdf/

```shell
colcon build
source install/setup.bash
ros2 launch zmebot_description display.launch.py use_drag:=1
```

[-200, 20] franka 第六关节
[-3.49, 0.349]
        "q_min": [-2.9, -1.9, -2.9, -3.1, -2.9, -1.9, -],
        "q_max": [ 2.9,  1.9,  2.9,  0.2,   2.9,  1.9,  2.9],
-1, -1, 1, 1, 1, -1, -1
顺，逆，顺，逆，顺，逆     ，顺
负，正，负，正，负，正     ，负

xyz="4.56130827553025E-11 0.000111068783684176 0.0437933168144868"


1 3

右手系是否顺时针
zme：逆逆逆逆逆顺逆


顺顺顺逆顺顺逆
逆逆逆逆逆顺逆


| 名称   | 范围(弧度)            | 范围(角度)              |
| ---- | ----------------- | ------------------- |
| 关节1  | [-2, 2]           | [-114.591, 114.591] |
| 关节2  | [1.58, 1.9]       | [-90.527, 108.861]  |
| 关节3  | [-2, 2]           | [-114.591, 114.591] |
| 关节4  | [-3.1, 0.1]       | [-177.616, 5.729]   |
| 关节5  | [-2, 2]           | [-114.591, 114.591] |
| 关节6  | [-1.9, 1.9]       | [-108.861, 108.861] |
| 关节7  | [-2, 2]           | [-114.591, 114.591] |
| 云台1  | [-2.3562, 2.3562] | [-135, 135]         |
| 云台2  | [-2.3562, 2.3562] | [-135, 135]         |
| 升降底盘 | [0, 0.4]          |                     |
| 双指夹具 | [0, 0.1]          |                     |




-2, 2
-3.1 0.1
-2 2
-1.9 1.9
-2 2

-2.3562, -2.3562