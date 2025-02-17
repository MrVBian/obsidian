[4.5安装](https://blog.csdn.net/Clam_dw/article/details/145447273)
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

交互脚本：[Isaac](https://docs.omniverse.nvidia.com/isaacsim/latest/gui_tutorials/tutorial_gui_interactive_scripting.html)

一些链接：
https://developer.nvidia.com/blog/author/asawareeb/

# 1 官方环境

```shell
./isaaclab.sh -p source/standalone/environments/list_envs.py
```

##  Isaac Lab Ecosystem
https://isaac-sim.github.io/IsaacLab/main/source/setup/ecosystem.html
![[Pasted image 20241212193905.png]]
![[Pasted image 20250214152435.png]]
![[Pasted image 20250214152443.png]]
[参考架构](https://isaac-sim.github.io/IsaacLab/main/source/refs/reference_architecture/index.html)

## 解决Isaac Sim资源获取不到问题

> Could not open asset @[http](https://so.csdn.net/so/search?q=http&spm=1001.2101.3001.7020)://omniverse-content-production

step1：
在Omniverse APP里点击 NUCLEUS 或者 Nucleus Navigator，选择自己要下载的 Isaac Sim 资源包：
![[Pasted image 20241225171621.png]]
step2:
打开对应版本的isaac sim安装目录，运行下面脚本（注意替换里面的目录）即可：
```shell
# 将目录替换成你自己的下载的即可
./isaac-sim --/persistent/isaac/asset_root/default="D:\omniverse\Downloads\Assets\Isaac\4.2"
# /home/zme/.local/share/ov/data/Kit/Isaac-Sim/4.2/user.config.json

# ./isaac-sim.sh --/persistent/isaac/asset_root/default="/home/zme/Documents/IsaacAssets"
```

```json
        "isaac": {
            "asset_root": {
                "default": "omniverse://localhost/NVIDIA/Assets/Isaac/2023.1.1",
                "nvidia": "omniverse://localhost/NVIDIA",
                "isaac": "omniverse://localhost/NVIDIA/Assets/Isaac/2023.1.1/Isaac",
                "cloud": "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/2023.1.1",
                "timeout": 10.0
            }
        },
```

```json
        "isaac": {
            "asset_root": {
                "nvidia": "omniverse://localhost/NVIDIA",
                "isaac": "omniverse://localhost/NVIDIA/Assets/Isaac/4.2/Isaac",
                "cloud": "http://omniverse-content-production.s3-us-west-2.amazonaws.com/Assets/Isaac/4.2",
                "timeout": 5.0,
                "default": "/home/zme/Documents/IsaacAssets"
            }
        },

```
上面指令的目的是改掉 **user.config.json** 这个文件，这个文件所在目录在你的DATA PATH下
![[Pasted image 20241225171752.png]]
