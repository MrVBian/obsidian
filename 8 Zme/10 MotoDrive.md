# Modbus RTU 通信协议规范

## 1. 指令格式 (主机->从机)

帧结构(8字节)：0x5A | (0x06 | 0x03) | Addr_H | Addr_L | Data_H | Data_L | CRC_H | CRC_L

| 字节           | 说明          |
| ------------ | ----------- |
| 0x5A         | 固定帧头        |
| 0x06 \| 0x03 | 写指令码 \| 读指令 |
| Addr_H       | 写入目标地址高字节   |
| Addr_L       | 写入目标地址低字节   |
| Data_H       | 写入数据高字节     |
| Data_L       | 写入数据低字节     |
| CRC_H        | CRC16校验值高字节 |
| CRC_L        | CRC16校验值低字节 |

## 2. 关键寄存器映射
### 2.1 主机对从机“写”
#### 2.1.1 指令格式
| 方向  | 帧结构                                                                 |
| --- | ------------------------------------------------------------------- |
| 请求帧 | `0x5A` + `0x06` + Addr_H + Addr_L + Data_H + Data_L + CRC_H + CRC_L |
| 响应帧 | `0x5A` + `0x06` + Addr_H + Addr_L + Data_H + Data_L + CRC_H + CRC_L |
#### 2.1.2 写入地址映射

##### Ⅰ 运行命令

| Addr_H + Addr_L | Data_H + Data_L | 指令名称    |
| --------------- | --------------- | ------- |
| 00x5000         | 0               | 停机      |
| 00x5000         | 1               | 运行      |
| 00x5000         | 2               | 复位      |
| 00x5000         | 3               | 电机初相位辨识 |
| 00x5000         | 4               | 机械零点给定  |
| 00x5000         | 5               | 开环VF    |
##### Ⅱ 指令给定

| Addr_H + Addr_L | Data_H + Data_L  | 指令名称   | 单位        | 描述                   |
| --------------- | ---------------- | ------ | --------- | -------------------- |
| 0xA000          | [0x0000, 0xFFFF] | 电流指令给定 | 0.1%      | signed short（正负代表方向） |
| 0xA001          | [0x0000, 0xFFFF] | 速度指令给定 | 1rpm      | signed short（正负代表方向） |
| 0xA002          | [0x0000, 0xFFFF] | 位置指令给定 | 0.1degree | signed short（正负代表方向） |
| 0xA003          | [0x0000, 0xFFFF] | 转矩指令给定 | 0.01Nm    | signed short（正负代表方向） |
##### Ⅲ 系统参数

| Addr_H + Addr_L | 参数名称        | 数据类型           | 单位值      | 最小值  | 最大值   |
| --------------- | ----------- | -------------- | -------- | ---- | ----- |
| 0x1000          | 电机极对数       | unsigned short | 1        | 1    | 20    |
| 0x1001          | 电机最大频率      | unsigned short | 0.1 Hz   | 500  | 7000  |
| 0x1002          | 电机额定频率      | unsigned short | 0.1 Hz   | 500  | 7000  |
| 0x1003          | 冗余频率        | unsigned short | 0.1 Hz   | 50   | 500   |
| 0x1004          | 电机额定电压      | unsigned short | 0.1 V    | 200  | 600   |
| 0x1005          | 电机额定电流      | unsigned short | 0.1 A    | 1    | 200   |
| 0x1006          | 电机额定扭矩      | unsigned short | 0.01 Nm  | 1    | 100   |
| 0x1007          | 电机定子电阻      | unsigned short | 0.001 Ω  | 1    | 5000  |
| 0x1008          | 电机D轴电感      | unsigned short | 0.001 mH | 1    | 5000  |
| 0x1009          | 电机Q轴电感      | unsigned short | 0.001 mH | 1    | 5000  |
| 0x100A          | 电机反电动势      | unsigned short | 0.1 V    | 1    | 600   |
| 0x100B          | 电机初相位高16位   | unsigned short | 1        | 0    | 65535 |
| 0x100C          | 电机初相位低16位   | unsigned short | 1        | 0    | 65535 |
|                 |             |                |          |      |       |
| 0x100D          | 载波周期计数值     | unsigned short | 1        | 2000 | 8000  |
| 0x100E          | 载波频率        | unsigned short | 0.1 kHz  | 100  | 400   |
| 0x100F          | 加速时间        | unsigned short | 0.1 S    | 1    | 100   |
| 0x1010          | 减速时间        | unsigned short | 0.1 S    | 1    | 100   |
| 0x1011          | 扭矩限定        | unsigned short | 0.1%     | 100  | 2000  |
| 0x1012          | 转速限定        | unsigned short | 1 RPM    | 0    | 5000  |
|                 |             |                |          |      |       |
| 0x1013          | 位置环Kp       | unsigned short | 1        | 0    | 100   |
| 0x1014          | 位置环Kd       | unsigned short | 1        | 0    | 200   |
| 0x1015          | 转速环Kp       | unsigned short | 1        | 0    | 100   |
| 0x1016          | 转速环积分时间     | unsigned short | 0.01 S   | 0    | 65535 |
| 0x1017          | 转速环Ki       | unsigned short | 1        | 0    | 65535 |
| 0x1018          | 电流环励磁Kp     | unsigned short | 1        | 0    | 50    |
| 0x1019          | 电流环励磁Ki     | unsigned short | 1        | 0    | 120   |
| 0x101A          | 电流环力矩Kp     | unsigned short | 1        | 0    | 50    |
| 0x101B          | 电流环力矩Ki     | unsigned short | 1        | 0    | 300   |
|                 |             |                |          |      |       |
| 0x101C          | 弱磁等级        | unsigned short | 1        | 0    | 2000  |
| 0x101D          | 过调系数        | unsigned short | 1        | 100  | 200   |
| 0x101E          | 弱磁深度        | unsigned short | 1        | 1    | 50    |
|                 |             |                |          |      |       |
| 0x101F          | V/F调制比      | unsigned short | 0.1%     | 10   | 10    |
| 0x1020          | V/F频率       | unsigned short | 0.1 Hz   | 1    | 65535 |
| 0x1021          | 初限位辨识励磁电流   | unsigned short | 0.1%     | 10   | 65535 |
|                 |             |                |          |      |       |
| 0x1022          | 减速器调速比      | unsigned short | 1        | 0    | 200   |
| 0x1023          | 抱闸使能        | unsigned short | 1        | 1    | 10000 |
| 0x1024          | 脱抱闸偏移角      | unsigned short | 1°       | 0    | 1     |
| 0x1025          | 脱抱闸误差角      | unsigned short | 1°       | 0    | 90    |
| 0x1026          | 脱抱闸力矩电流     | unsigned short | 0.1%     | 10   | 200   |
| 0x1027          | 扭矩传感器偏移量    | unsigned short | 1        | 0    | 1     |
|                 |             |                |          |      |       |
| 0x1028          | 电机应用位置      | unsigned short | 1        | 0    | 4     |
| 0x1029          | 系统ID        | unsigned short | 1        | 0    | 25    |
| 0x102A          | 机械零位多圈计数值   | unsigned short | 1        | 0    | 65535 |
| 0x102B          | 机械正限位值(电机端) | unsigned short | 0.1°     | 0    | 3600  |
| 0x102C          | 机械负限位值(电机端) | unsigned short | 0.1°     | 0    | 3600  |
| 0x102D          | 机械零位单圈高16位  | unsigned short | 1        | 0    | 65535 |
| 0x102E          | 机械零位单圈低16位  | unsigned short | 1        | 0    | 65535 |
|                 |             |                |          |      |       |
| 0x102F          | 系统最大电流      | unsigned short | 0.1 A    | 1    | 500   |
| 0x1030          | 系统额定电压      | unsigned short | 0.1 V    | 200  | 600   |
| 0x1031          | 电流矫正系数      | unsigned short | 0.1%     | 512  | 2048  |
| 0x1032          | 电压矫正系数      | unsigned short | 0.1%     | 512  | 2048  |
### 2.2 主机对从机“读”

#### 2.2.1 指令格式
| 方向  | 帧结构                                                                                 |
| --- | ----------------------------------------------------------------------------------- |
| 请求帧 | `0x5A` + `0x03` + Addr_H + Addr_L + Data_H + Data_L + CRC_H + CRC_L                 |
| 响应帧 | `0x5A` + `0x03` + Data_Len_H + Data_Len_L + Data1_H + Data1_L + ... + CRC_H + CRC_L |

| 字段                  | 说明          |
| ------------------- | ----------- |
| 0x03                | 读指令标识       |
| Data_Len+Data_Len_L | 从机实际返回的数据数量 |
| Datax_H+Datax_L     | 返回的第x个寄存器数据 |

#### 2.2.2 读取地址映射
##### Ⅰ 系统参数 (0x1000 - 0x1032)

![[10 MotoDrive#Ⅲ 系统参数]]

##### Ⅱ 实时数据读取 (0x4000 - 0x4021)
| Addr_H + Addr_L | 参数名称        | 数据类型           | 单位    | 图表Y轴名称          |
| --------------- | ----------- | -------------- | ----- | --------------- |
| 0x4000          | 电机电角度       | unsigned short | 0.01° | 电机电角度 (0.01°)   |
| 0x4001          | 电流环力矩电流给定值  | short          | 0.1A  | 力矩电流给定值 (0.1A)  |
| 0x4002          | 电流环力矩电流反馈值  | short          | 0.1A  | 力矩电流反馈值 (0.1A)  |
| 0x4003          | 电流环励磁电流给定值  | short          | 0.1A  | 励磁电流给定值 (0.1A)  |
| 0x4004          | 电流环励磁电流反馈值  | short          | 0.1A  | 励磁电流反馈值 (0.1A)  |
| 0x4005          | 设定转速        | short          | 1 rpm | 设定转速 (rpm)      |
| 0x4006          | 运行转速        | short          | 1 rpm | 运行转速 (rpm)      |
| 0x4007          | 设定角度        | short          | 0.1°  | 设定角度 (0.1°)     |
| 0x4008          | 运行角度        | short          | 0.1°  | 运行角度 (0.1°)     |
| 0x4009          | 系统标志位       | unsigned short | -     | 系统标志位 (bit)     |
| 0x400A          | 故障代码        | unsigned short | -     | 故障代码 (code)     |
| 0x400B          | 力矩电流滤波值     | short          | 0.1A  | 力矩电流滤波值 (0.1A)  |
| 0x400C          | 励磁电流滤波值     | short          | 0.1A  | 励磁电流滤波值 (0.1A)  |
| 0x400D          | 电流环力矩调节器输出  | short          | -     | 力矩调节器输出 (LSB)   |
| 0x400E          | 电流环力矩调节器积分值 | short          | -     | 力矩调节器积分值 (LSB)  |
| 0x400F          | 电流环励磁调节器输出  | short          | -     | 励磁调节器输出 (LSB)   |
| 0x4010          | 电流环励磁调节器积分值 | short          | -     | 励磁调节器积分值 (LSB)  |
| 0x4011          | 位置环输出       | short          | -     | 位置环输出 (LSB)     |
| 0x4012          | 速度环输出       | short          | -     | 速度环输出 (LSB)     |
| 0x4013          | 速度环积分值      | short          | -     | 速度环积分值 (LSB)    |
| 0x4014          | Q轴输出电压      | short          | 0.1V  | Q轴电压 (0.1V)     |
| 0x4015          | D轴输出电压      | short          | 0.1V  | D轴电压 (0.1V)     |
| 0x4016          | U相实时电流值     | short          | 0.1A  | U相电流 (0.1A)     |
| 0x4017          | V相实时电流值     | short          | 0.1A  | V相电流 (0.1A)     |
| 0x4018          | W相实时电流值     | short          | 0.1A  | W相电流 (0.1A)     |
| 0x4019          | 输入直流电压      | short          | 0.1V  | 直流电压 (0.1V)     |
| 0x401A          | 机械角度        | unsigned short | 0.01° | 机械角度 (0.01°)    |
| 0x401B          | 输出电流有效值     | unsigned short | 0.1A  | 电流有效值 (0.1A)    |
| 0x401C          | 输出电压有效值     | unsigned short | 0.1V  | 电压有效值 (0.1V)    |
| 0x401D          | MOSFET温度    | unsigned short | 0.1℃  | MOSFET温度 (0.1℃) |
| 0x401E          | 电机温度        | unsigned short | 0.1℃  | 电机温度 (0.1℃)     |
| 0x401F          | 输出扭矩        | short          | 0.1Nm | 输出扭矩 (0.1Nm)    |
| 0x4020          | 输出功率        | short          | 0.1W  | 输出功率 (0.1W)     |
| 0x4021          | 未使用         | -              | -     |                 |

## 3 错误帧格式
帧结构：`0x5A` + `0x5A` + Code

| Code | 错误类型    | 描述                       |
| ---- | ------- | ------------------------ |
| 1    | CRC校验错误 | 帧校验码(CRC)不匹配             |
| 2    | 命令错误    | 指令码非0x03(读)或0x06/0x03(写) |
| 3    | 地址错误    | 请求地址超出有效范围               |
| 4    | 数据错误    | 写入值超出允许范围                |


# 10
```shell
docker run -p 9000:9000 -p 9090:9090 \
     --net=host \
     --name minio \
     -d --restart=always \
     -e "MINIO_ACCESS_KEY=admin" \
     -e "MINIO_SECRET_KEY=12345678" \
     -v /home/zme/Software/minio/data:/data \
     -v /home/zme/Software/minio/config:/root/.minio \
     minio/minio server \
     /data --console-address ":9090" -address ":9000"
```