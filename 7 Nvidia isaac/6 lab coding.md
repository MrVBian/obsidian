```shell
./isaaclab.sh -p zmeisaac/base/test.py --num_envs 100
./isaaclab.sh -p zmeisaac/base/test2.py --task=Isaac-Cartpole-Direct-v0
./isaaclab.sh -p zmeisaac/base/sim.py


./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task Isaac-Velocity-Rough-H1-v0 --headless
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py --task Isaac-Velocity-Rough-H1-v0 --num_envs 64 --checkpoint logs/rsl_rl/h1_rough/2025-02-19_17-52-02/model_2999.pt
./isaaclab.sh -p scripts/tutorials/03_envs/policy_inference_in_usd.py --checkpoint logs/rsl_rl/h1_rough/2025-02-19_17-52-02/exported/policy.pt



# 拉抽屉
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/train.py --task Isaac-Franka-Cabinet-Direct-v0
./isaaclab.sh -p scripts/reinforcement_learning/rsl_rl/play.py --task Isaac-Franka-Cabinet-Direct-v0 --checkpoint logs/rsl_rl/franka_cabinet_direct/2025-02-20_14-09-36/model_1499.pt

# Zme拉抽屉
```

学习笔记：[Isaac Lab Hub](https://lycheeai.notion.site/Isaac-Lab-Hub-17928763942b808289f4c2f01154954d)
# 0 术语
- Markov Decision Processes（MDP）  
- 观察、行动、讲理、终止、事件
- Manager Framework Classes（MDP）管理器框架类
# 1 Manager Based Workflow 基于管理器的工作流

| name                | 名称    | 作用                           |
| ------------------- | ----- | ---------------------------- |
| Action Manager      | 动作管理器 | 定义并应用RL agent与环境交互时可以采取的动作   |
| Observation Manager | 观察管理器 | 向RL agent提供必要的状态信息（观察值）以做出决策 |
| Reward Manager      | 奖励管理器 | 指定RL agent为指导学习而获得的奖励        |
| Termination Manager | 终止管理器 | 指定结束的条件（例如，失败或时间限制）          |
| Curriculum Manager  | 课程管理器 | 随着agent的学习动态调整环境的难度          |
| Command Manager     | 命令管理器 | 定义用于直接控制机器人或实体的特定命令          |
![[Pasted image 20250214152435.png]]
- CartpoleSceneCfg

```python
# Post initialization
def_post_init_(self)-> None:
	"""Post initialization."""
	self.decimation = 2 # 渲染频率是模拟步骤频率的一半
	self.episode_length_s = 5 # 设置模拟环境中每个回合的最大时长为 5 秒
	self.viewer.eye = (8.0,0.0,5.0) # 可视化窗口中相机的初始位置
	self.sim.dt = 1 / 120 # 设置模拟的频率为 120 Hz
	self.sim.render_interval = self.decimation # 控制渲染的频率，渲染频率是模拟频率的一半
```
# 2 Direct Workflow 直接工作流程
基于Manager的工作流程为大型复杂环境提供了模块化和可扩展性，而Direct Workflow则提供了更简单的整体式结构。所有环境逻辑（包括奖励、观察、重置和终止）都在一个类中实现，没有管理器。它还允许对环境的关键部分使用PyTorch、JIT等性能提升工具。
![[Pasted image 20250214152443.png]]
```python
action_scale = 100.0  # 用于将智能体（agent）输出的动作值映射到实际应用于环境的力的大小
action_space = 1      # 环境中可用的动作数量 (1:只有一个动作，即对小车施加力)
observation_space = 4 # 环境中提供给智能体的观测信号的数量 (小车和杆子的 positions/velocities)

# 在对称的(actor-critic)算法中，(critic)没有单独定义的状态空间。
# 通常，在(actor-critic)算法中，(actor)负责选择动作，(critic)负责评估状态的价值。
# 当 state_space 为 0 时，表示(critic)使用与(actor)相同的状态信息。
state_space = 0
```
