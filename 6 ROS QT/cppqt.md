

# UI转Cpp
```shell
uic -o ui_zmeui.h zmeui.ui
```

## 替换
```text
icon.addFile(QString::fromUtf8("../../../robot.png"), QSize(), QIcon::Normal, QIcon::Off)
```
```text
icon.addFile(QString::fromStdString(ament_index_cpp::get_package_share_directory(pkg_name) + "/resources/ZmeUi.png"), QSize(), QIcon::Normal, QIcon::Off);
```

```text
fromUtf8("../resources/
```

```text
fromStdString(ament_index_cpp::get_package_share_directory(pkg_name) + "/resources/
```


| 名称  | 范围(弧度)             | 范围(角度)              |
| --- | ------------------ | ------------------- |
| 关节1 | [-2, 2]            | [-114.591, 114.591] |
| 关节2 | [1.58, 1.9]        | [-90.527, 108.861]  |
| 关节3 | [-2, 2]            | [-114.591, 114.591] |
| 关节4 | [-3.1, 0.1]        | [-177.616, 5.729]   |
| 关节5 | [-2, 2]            | [-114.591, 114.591] |
| 关节6 | [-1.9, 1.9]        | [-108.861, 108.861] |
| 关节7 | [-2, 2]            | [-114.591, 114.591] |
| 云台1 | [-2.3562, -2.3562] | [-135, 135]         |
| 云台2 | [-2.3562, -2.3562] | [-135, 135]         |

1 首先创建ros2功能包:
```shell
ros2 pkg create --build-type ament_cmake zme_ui --dependencies rclcpp std_msgs rviz_common
```
2 创建面板插件类


```cpp
#include <QMessageBox>
QMessageBox::information(nullptr, "提示", "这是一段文字。");
```