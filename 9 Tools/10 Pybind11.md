[pybind11 中文文档](https://geekdaxue.co/read/pybind11-CN/summary.md#bj05n5)
```shell
g++ -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` 要编译的源代码 -o 模块名`python3-config --extension-suffix` -I /path/to/python3

c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)
```
# 样例
以下是一个完整的 CMake工程样例，支持多文件、Eigen依赖和Pybind11绑定，可直接复制使用。
## Eigen安装
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
## 1 工程目录结构
```bash
pybind_eigen_demo/
├── CMakeLists.txt          # CMake主配置文件
├── include/                # 自定义头文件
│   └── MathUtils.h        
├── src/                    # C++核心实现
│   └── MathUtils.cpp      
└── bind/                   # Pybind11绑定代码
    └── bind.cpp
```
## 2 各文件内容
### 2.1 `include/MathUtils.h`
```cpp
#pragma once
#include <Eigen/Dense>  // Eigen头文件

class MathUtils {
public:
    // 计算两个向量的点积（Eigen::Vector3d类型）
    static double dot_product(const Eigen::Vector3d& a, const Eigen::Vector3d& b);

    // 计算三个向量的混合积（调用dot_product）
    static double triple_product(
        const Eigen::Vector3d& a,
        const Eigen::Vector3d& b,
        const Eigen::Vector3d& c
    );
};
```
### 2.2 `src/MathUtils.cpp`
```cpp
#include "MathUtils.h"

double MathUtils::dot_product(const Eigen::Vector3d& a, const Eigen::Vector3d& b) {
    return a.dot(b);
}

double MathUtils::triple_product(const Eigen::Vector3d& a, const Eigen::Vector3d& b, const Eigen::Vector3d& c) {
    Eigen::Vector3d cross = b.cross(c);
    return dot_product(a, cross);  // 调用第一个函数
}
```
### 2.3 `bind/bind.cpp`（Pybind11绑定）
```cpp
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>  // 支持Eigen类型自动转换
#include "MathUtils.h"

namespace py = pybind11;

// 绑定MathUtils类
PYBIND11_MODULE(math_utils, m) {
    py::class_<MathUtils>(m, "MathUtils")
        .def_static("dot_product", &MathUtils::dot_product,
            py::arg("a"), py::arg("b"),
            "计算两个三维向量的点积")
        .def_static("triple_product", &MathUtils::triple_product,
            py::arg("a"), py::arg("b"), py::arg("c"),
            "计算三个三维向量的混合积 (a · (b × c))");
}
```
### 2.4 `CMakeLists.txt`（核心配置）
```cmake
cmake_minimum_required(VERSION 3.15)
project(pybind_eigen_demo)

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 查找依赖库
find_package(Eigen3 REQUIRED)          # 查找Eigen
find_package(pybind11 REQUIRED)        # 查找Pybind11

# 添加Pybind11模块
pybind11_add_module(math_utils        # 生成的Python模块名
    bind/bind.cpp                     # 绑定代码
    src/MathUtils.cpp                 # 核心实现
)

# 包含头文件路径
target_include_directories(math_utils PRIVATE
    ${EIGEN3_INCLUDE_DIR}             # Eigen头文件
    ${PROJECT_SOURCE_DIR}/include      # 自定义头文件
)

# 可选：设置输出目录（Unix下默认在build目录）
set_target_properties(math_utils PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)
```
## 3 构建与编译
### 3.1 创建构建目录
```shell
mkdir build && cd build
```
### 3.2 生成构建系统
```shell
cmake .. -DCMAKE_BUILD_TYPE=Release
```
### 3.3 编译
```shell
cmake --build . --config Release
```
### **3.4 输出文件**
编译完成后，生成的Python模块（如`math_utils.cpython-310-x86_64-linux-gnu.so`）会出现在`build/bin`目录。
## 4 Python调用示例
```python
import numpy as np
from math_utils import MathUtils

# 定义三个三维向量
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
c = np.array([7.0, 8.0, 9.0])

# 计算点积
dot = MathUtils.dot_product(a, b)
print(f"点积: {dot}")  # 输出: 32.0

# 计算混合积
triple = MathUtils.triple_product(a, b, c)
print(f"混合积: {triple}")  # 输出: 0.0（因为三个向量共面）
```
## 5 关键规则总结
1. **头文件顺序**：在绑定代码中**先包含Eigen头文件**，再包含Pybind11头文件，避免宏冲突。
2. **Eigen类型支持**：使用`#include <pybind11/eigen.h>`实现Eigen与NumPy的自动类型转换。
3. **模块命名**：`PYBIND11_MODULE(math_utils, m)`中的模块名需与`pybind11_add_module`中的名称一致。
4. **CMake配置**：
    - 使用`find_package(Eigen3)`和`find_package(pybind11)`自动定位依赖。
    - `pybind11_add_module`简化模块生成流程。
5. **跨平台兼容**：CMake自动处理不同操作系统的库后缀（如`.so`或`.pyd`）。