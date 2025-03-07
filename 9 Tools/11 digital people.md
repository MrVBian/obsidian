插件：
- [AIGODLIKE-ComfyUI-Translation](https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation)
- [CosyVoice-ComfyUI](https://github.com/AIFSH/CosyVoice-ComfyUI)
- [ComfyUI_EchoMimic](https://github.com/smthemex/ComfyUI_EchoMimic)
# ComfyUI

```shell
conda create -n comfyui python=3.12
conda activate comfyui

git clone https://github.com/comfyanonymous/comfyui.git
cd comfyui
pip install -r requirements.txt

cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
pip install GitPython
python main.py --listen 0.0.0.0 --port 8188
```

```shell
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

https://github.com/YanWenKun/ComfyUI-Docker?tab=readme-ov-file
```shell
mkdir -p storage

docker run -it --rm \
  --name comfyui-cu124 \
  --gpus all \
  -p 8188:8188 \
  -v "$(pwd)"/storage:/root \
  -e CLI_ARGS="" \
  yanwk/comfyui-boot:cu124-slim
```
