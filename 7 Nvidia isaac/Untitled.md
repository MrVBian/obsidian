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


我希望在nvidia isaac中模拟一款真实相机。真实相机工作距离为[0.2m,5m]，FOV：H86° V55° D93.5°。我在isaac相机中找到的属性有：Focal Length、Focus Distance、fStop、Horizontal Aperture、Vertical Aperture。请问我该如何配置isaac仿真中的相机属性，才能尽可能模拟真实相机


真实相机具体参数如下：

| 参数名称   | 数值         |
| ------ | ---------- |
| H FOV  | 86°        |
| V FOV  | 55°        |
| D FOV  | 93.5°      |
| 分辨率比例  | 16:9       |
| 传感器对角线 | **28.2mm** |
| 传感器比例  | 16:9       |

求水平光圈尺寸、垂直光圈尺寸、focal length和focus distance。请给出最终结果，保留两位小数


多相机视图，帧率很低。
当我只有一个视图时，帧率在60hz，当我启动四个视图时，帧率为13.7hz，但是主机的性能并没有发挥完，在CPU、GPU和内存上依然有较大冗余。
问题：
1、这是什么原因？
2、有什么优化方法？


### Isaac Sim Version
4.2.0
### Operating System
Ubuntu 22.04

红色轮子(带drive)，蓝色万向轮(无drive)，绿色万向轮的转向(无drive)。红色轮子施加相反的力，正常情况应该是自转。
问题：地面平坦，运行中会被弹开


 Warning: in _ReportErrors at line 2890 of /builds/omniverse/usd-ci/USD/pxr/usd/usd/stage.cpp -- In </World/envs/env_0/Robot>: Could not open asset @http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.2/Isaac/IsaacLab/Robots/Classic/Cartpole/cartpole.usd@ for reference introduced by @anon:0x652bf7c76f00:World0.usd@</World/envs/env_0/Robot>. (recomposing stage on stage @anon:0x652bf7c76f00:World0.usd@ <0x652bf61e5660>)



如下基于isaac lab的python代码启动isaac sim4.2：
```python
import argparse
from omni.isaac.lab.app import AppLauncher
parser = argparse.ArgumentParser(description="Pour wine stage.")    # create argparser
AppLauncher.add_app_launcher_args(parser)   # append AppLauncher cli args
args_cli = parser.parse_args()              # parse the arguments
# app_launcher = AppLauncher(args_cli, settings={"rendering/preset": "Medium"})
app_launcher = AppLauncher(args_cli)        # launch omniverse app
simulation_app = app_launcher.app
"""Rest everything follows."""
from omni.isaac.lab.sim import SimulationCfg, SimulationContext

def main():
    sim_cfg = SimulationCfg(dt=0.01, device=args_cli.device)
    sim = SimulationContext(sim_cfg)
    world = World(stage_units_in_meters=1.0)
    world.reset()

    while simulation_app.is_running():
        sim.step()  # step
```


以下是isaac lab推荐的机器人控制代码
```python
            # reset the scene entities
            # root state
            # we offset the root state by the origin since the states are written in simulation world frame
            # if this is not done, then the robots will be spawned at the (0, 0, 0) of the simulation world
            root_state = robot.data.default_root_state.clone()
            root_state[:, :3] += origins
            robot.write_root_link_pose_to_sim(root_state[:, :7])
            robot.write_root_com_velocity_to_sim(root_state[:, 7:])
            # set joint positions with some noise
            joint_pos, joint_vel = robot.data.default_joint_pos.clone(), robot.data.default_joint_vel.clone()
            joint_pos += torch.rand_like(joint_pos) * 0.1
            robot.write_joint_state_to_sim(joint_pos, joint_vel)
            # clear internal buffers
            robot.reset()
```
下面是我写的版本，targetPositions是关节值，弧度
```python
            targetPositions = []

            # 如果在目标关节角度字典中，则使用目标角度，否则使用当前角度
            for i in range(len(jointName)):
                if jointName[i] in jointTargets:
                    targetPositions.append(jointTargets[jointName[i]])
                else:
                    targetPositions.append(0)  # 维持当前角度
            dc.set_articulation_dof_position_targets(art, targetPositions)
```
我的版本中set_articulation_dof_position_targets是错的，帮我改成isaac lab推荐的版本



isaaclab下用vscode开发
```python
from isaaclab_assets import H1_CFG
```
以上代码，可以正确运行，但是VSCode没办法跳转到H1_CFG下，如何配置VSCode，可以使其正常跳转