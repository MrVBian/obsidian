Isaac Sim 6.0 中双臂七轴机械臂与二自由度夹爪关节动力学参数的 Gain Tuner 优化咨询

**【背景】**

- 仿真平台：Isaac Sim 6.0
- 机器人对象：双臂七轴机械臂，末端配置二自由度夹爪；夹爪关节为旋转关节。
- 当前目标：配置并优化各关节的动力学参数，使整体动力学响应合理、稳定，并满足控制需求。
- 调参工具：Gain Tuner / Property 面板。

**【当前 Gain Tuner 配置】**

- Test Mode：Step Function
- Test Duration：5 s
- Drive Type：全部为 Force
- 待优化/检查参数：Mass、Stiffness、Damping
- 参数来源：Gain Tuner / Property 面板
- 关节类型：机械臂为七轴旋转关节；夹爪为二自由度旋转关节。
- 缺少的动力学参数，都是缺省状态

**【已有数据】**

| 关节        | Mass    | Stiffness | Damping |
| ----------- | ------- | ---- | ----------- |
| left_joint1 | 0.05506 | 0 | 0 |
| left_joint2 | 0.28739 | 0 | 0 |
| left_joint3 | 0.19116 | 0 | 0 |
| left_joint4 | 0.14986 | 0 | 0 |
| left_joint5 | 0.14731 | 0 | 0 |
| left_joint6 | 0.05075 | 0 | 0 |
| left_joint7 | 0.07375 | 0 | 0 |
| left_gripper_finger_joint1 | 0.14125 | 0 | 0 |
| left_gripper_finger_joint2 | 0.14125 | 0 | 0 |
|  |  | | |
| right_joint1 | 0.05506 | 0 | 0 |
| right_joint2 | 0.28739 | 0 | 0 |
| right_joint3 | 0.19116 | 0 | 0 |
| right_joint4 | 0.14986 | 0 | 0 |
| right_joint5 | 0.14731 | 0 | 0 |
| right_joint6 | 0.05075 | 0 | 0 |
| right_joint7 | 0.07375 | 0 | 0 |
| right_gripper_finger_joint1 | 0.14125 | 0 | 0 |
| right_gripper_finger_joint2 | 0.14125 | 0 | 0 |

### 场景

- https://github.com/YoottaAI/World-SimReady-Home

- https://github.com/LightwheelAI/Lightwheel_Kitchen

- https://huggingface.co/LightwheelAI/leisaac_env/tree/main

### 视频

- https://www.bilibili.com/video/BV1dNR7B5EwP/?vd_source=4f10315acd30a6491a3fb1f267a3a517





```shell
docker run -it -d --name xr_isaac \
  --restart always \
  -w /projects \
  -v /home/zme/pico_tele_zme_isaac:/projects \
  -v /dev/bus/usb:/dev/bus/usb \
  --privileged \
  --net=host \
  ros_humble_xr_zme_x86:v4 \
  /usr/bin/supervisord -c /etc/supervisor/conf.d/myprograms.conf
```



- **状态区分**：有数据是绿色实心圆点加呼吸光晕，无数据是灰色空心细环，未连接是浅灰色虚线环。三类状态靠形状和颜色双重区分，不依赖文字也能认。
- **重启**：docker restart xr_x86
- **Topic**：/tele_vr_cmd



- scene5.1

  - 冰箱交互

- hotel

  - 门/窗交互

  - 推拉门交互

- le
  - kitchen
    - 柜子交互
  - toyroom
    - 堆积木
  - bedroom
    - 叠衣服
    - 晾衣架
- light_kitchen
  - 冰箱
  - 抽屉交互







docker 基于 **`humble-ros-base`**，容器。需要：

1. 安装glog-0.7.1
2. 设置时区为上海
3. 拉取ros代码后，colcon编译
4. 容器启动时，默认运行/projects/1start_xr.sh和/projects/2start_xr.sh

以上是一个镜像的构建，我希望尽量让容器体积小一些，如何实现





列出已注册的任务，然后查看任务相关的帮助：

```shell
uv run python scripts/environments/list_envs.py
uv run isaaclab train --rl_library rsl_rl --task Isaac-Open-Drawer-Franka-Direct --help
```

source/isaaclab_tasks/isaaclab_tasks/core/cabinet/config/franka/cabinet_direct_env_cfg.py


/home/zme/Software/RustDeskServer/docker-compose.yml内容如下：
```yml
version: '3'

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:latest
    command: hbbs -r 172.24.3.132:21117 -k _
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:latest
    command: hbbr -k _
    volumes:
      - ./data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```
我提供了一个py3代码和一个rustdesk的docker配置。我需要修改py代码，增加如下功能：
1、发现ip变动时，原先逻辑不变，同时修改rustdesk 客户端的ID/中继服务器地址为此ip；
2、rustdesk基于新ID/中继服务器地址更新生效


```shell
uv run isaaclab train --rl_library rsl_rl --task Isaac-Open-Drawer-Franka-Direct --num_envs 32 --visualizer kit --max_visible_envs 32 physics=isaacsim_physx


uv run isaaclab train 
  --rl_library rsl_rl 
  --task Isaac-Open-Drawer-Zmebot-Left-Direct 
  --num_envs 36 
  --visualizer kit 
  --max_visible_envs 36 
  physics=isaacsim_physx 
  env.sim.dt=0.004166666666666667 
  env.decimation=4
  
# Visual Train
uv run isaaclab train \
  --rl_library rsl_rl \
  --task Isaac-Open-Drawer-Zmebot-Left-Direct \
  --num_envs 256 \
  --visualizer kit \
  --max_visible_envs 256 \
  --checkpoint latest \
  --max_iterations 400 \
  physics=isaacsim_physx \
  env.sim.dt=0.004166666666666667 \
  env.decimation=4
  
# train
uv run isaaclab train \
  --rl_library rsl_rl \
  --task Isaac-Open-Drawer-Zmebot-Left-Direct \
  --num_envs 36 \
  --visualizer none \
  --checkpoint latest \
  --max_iterations 200 \
  physics=isaacsim_physx \
  env.sim.dt=0.004166666666666667 \
  env.decimation=4
  
 # Debug
uv run isaaclab play \
  --rl_library rsl_rl \
  --task Isaac-Open-Drawer-Zmebot-Left-Direct \
  --num_envs 1 \
  --visualizer kit \
  --max_visible_envs 1 \
  --checkpoint latest \
  --train_env_cfg \
  --real-time \
  physics=isaacsim_physx \
  env.sim.dt=0.004166666666666667 \
  env.decimation=4 \
  env.sim.render_interval=4 \
  env.debug_grasp=true
  
 --checkpoint /home/zme/isaaclab/IsaacLab/logs/rsl_rl/franka_open_drawer_direct/你的训练时间目录/model_399.pt
 
 /home/zme/isaaclab/IsaacLab/source/isaaclab_tasks/isaaclab_tasks/core/cabinet/config/franka
```

在 **Isaac Labv3.0.0-EA 项目根目录**运行上面这条命令，即可开启 Isaac Sim 窗口，并让 **32 台 Franka 机器人并行训练**。

以上是没问题的，我想要用我的机器人训练同样的任务，我的机器人是双臂七轴，夹爪是两自由度的。机器人路径是f"/home/zme/Documents/IsaacSim/Resources/urdf/src/zmebot_lite_description/urdf/zmebot_lite_description/zmebot_lite_description.usda"

关节初始姿态为：

​        joint_pos={
​            "right_joint1": -2.6179,
​            "right_joint2": 1.5707,
​            "right_joint3": 1.5707,
​            "right_joint4": -2.8797,
​            "right_joint5": 0.0,
​            "right_joint6": 1.3962,
​            "right_joint7": 0.0,
​            "right_gripper_finger_joint.*": 0.0,
​            "left_joint1": -2.6179,
​            "left_joint2": 1.5707,
​            "left_joint3": 1.5707,
​            "left_joint4": -2.8797,
​            "left_joint5": 0.0,
​            "left_joint6": 1.3962,
​            "left_joint7": 0.0,
​            "left_gripper_finger_joint.*": 0.0,
​        },

指导我，如何用我的机器人训练同样的任务(仅用左臂，右臂保持初始姿态即可)，训练左臂开抽屉。由于目标环境在远程，故将Franka 机器人强化学习的原始文件附加到上下文中





alias isaac='/home/zme/.local/share/ov/pkg/isaac-sim-4.2.0/isaac-sim.sh --/isaac/startup/ros_bridge_extension=omni.isaac.ros2_bridge --/rtx/ecoMode/enabled=True'
alias isaac5='/home/zme/Software/isaac-sim-4.5.0/isaac-sim.sh --/isaac/startup/ros_bridge_extension=isaacsim.ros2_bridge --/rtx/ecoMode/enabled=True'
alias isaac5s='/home/zme/Software/isaac-sim-4.5.0/isaac-sim.selector.sh'
