# 1 安装eigen
```shell
#安装
cd eigen-git-mirror
mkdir build
cd build
cmake ..
sudo make install
 
#安装后,头文件安装在/usr/local/include/eigen3/
#移动头文件
sudo cp -r /usr/local/include/eigen3/Eigen /usr/local/include 
```
# 2 转换so
```shell
c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)
```