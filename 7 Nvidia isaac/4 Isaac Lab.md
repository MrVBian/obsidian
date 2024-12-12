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

Isaac Python环境
```shell
/home/zme/.local/share/ov/pkg/isaac-sim-4.2.0/python.sh your_script.py

# 依赖项路径
# pip install -r /home/zme/.local/share/ov/pkg/isaac-sim-4.2.0/requirements.txt
```

# 1
