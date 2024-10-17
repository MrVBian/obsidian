

> [!warning] 英伟达独显驱动引起的Could not initialize shared resources for X11GraphicsDevice
> 在启动MATLAB时指定使用软件渲染模式而不是硬件加速的OpenGL模式
> matlab -softwareopengl

解决快捷方式问题
```shell
sudo vim /usr/share/applications/matlab.desktop 
```
 > 修改Exec为  Exec=matlab -desktop -softwareopengl


```matlab
path_urdf='/home/zme/project/ros/simulation_ws/zmebot_description/urdf/zme2_4/urdf/'
filename_urdf='zme2_4.urdf'
```

```shell
[filename_urdf, path_urdf] = uigetfile('*.urdf');
robot_urdf = importrobot([path_urdf, filename_urdf]);
show(robot_urdf)

# 可交互
interactiveGUI = interactiveRigidBodyTree(robot_urdf);
```