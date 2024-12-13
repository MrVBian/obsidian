# 0 概述
https://isaac-sim.github.io/IsaacLab/main/source/setup/installation/pip_installation.html
```shell
conda create -n isaaclab python=3.10


conda activate isaaclab

pip install --upgrade pip
pip install pyyaml typeguard
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu121
```
Isaac Lab
```shell
pip install isaacsim-rl isaacsim-replicator isaacsim-extscache-physics isaacsim-extscache-kit-sdk isaacsim-extscache-kit isaacsim-app --extra-index-url https://pypi.nvidia.com

# export isaac_path=/home/zme/.local/share/ov/pkg/isaac-sim-4.2.0
git clone git@github.com:isaac-sim/IsaacLab.git && cd IsaacLab
sudo apt install cmake build-essential
./isaaclab.sh --install # or "./isaaclab.sh -i"
```

安装测试
```shell
# Option 1: Using the isaaclab.sh executable
# note: this works for both the bundled python and the virtual environment
./isaaclab.sh -p source/standalone/tutorials/00_sim/create_empty.py

# Option 2: Using python in your virtual environment
python source/standalone/tutorials/00_sim/create_empty.py
```

Isaac Python环境
```shell
/home/zme/.local/share/ov/pkg/isaac-sim-4.2.0/python.sh your_script.py

# 依赖项路径
# pip install -r /home/zme/.local/share/ov/pkg/isaac-sim-4.2.0/requirements.txt
```

一些链接：
https://developer.nvidia.com/blog/author/asawareeb/

# 1 官方环境

```shell
./isaaclab.sh -p source/standalone/environments/list_envs.py
```

##  Isaac Lab Ecosystem
https://isaac-sim.github.io/IsaacLab/main/source/setup/ecosystem.html
![[Pasted image 20241212193905.png]]

[参考架构](https://isaac-sim.github.io/IsaacLab/main/source/refs/reference_architecture/index.html)