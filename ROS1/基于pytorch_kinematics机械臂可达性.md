# 1 环境配置

[[基于Reuleaux机械臂可达性|ROS环境]]
[[Python Env]]
```shell
pip install --upgrade pip==9.0.3  
pip install --upgrade setuptools

apt-get -y install python3-pip
```
# 2 问题

> [!question]
> lxml.etree.XML ValueError for Unicode string
> ```python
> data.read().encode()
> ```

> [!question]
> torch.det(J @ torch.transpose(J,1,2)).cpu() ^ SyntaxError: invalid syntax
> ```python
> # @运算符:其作用类似于torch.matmul
> a = torch.randn(2, 3, 4)
> b = torch.randn(2, 4, 5)
> print(torch.matmul(a, b).size())
> print((a @ b).size())
> ```

# 3 使用
```shell
# 每秒显示nvidia-smi
watch -n 1 nvidia-smi 

roscore
rosrun rviz rviz

export ROBOT=zmebot_dual_manipulator
rosrun tf static_transform_publisher 0 0 0 0 0 0 1 world base_footprint 100
rosrun map_creator load_reachability_map ur5.h5

roscore
# Rviz下，添加ReachabilityMap后，topic：/reachability_map
rosrun rviz rviz

# apt-get install ros-kinetic-rqt-tf-tree
rosrun rqt_tf_tree rqt_tf_tree
```


