
```shell
# qt 找不到文件 qpa/qplatformnativeinterface.h _
sudo apt-get install qtbase5-private-dev

# Could NOT find SDL_image (missing:SDL_IMAGE_LIBRARIES SDL_IMAGE_INCLUDE_DIRS)
sudo apt-get install libsdl-image1.2-dev
```

# 安装卸载
```shell
sudo snap install qtcreator-ros --classic
# 卸载
# sudo snap remove qtcreator-ros
```

# UI转python
```shell
pip install pyqt5-tools

pyuic5 -x yourform.ui -o file.py
```