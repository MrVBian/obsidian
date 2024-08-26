# 1 WebGL
## 1.1 接口
**请求方式：WebSocket**
**Topic：robot/robot/robot_id**（robot_id是变量）
**指令说明：桁架设备数采的数据通信接口**
```json
{
    "header":{
        "msg_type": ""
    },
    "data":{
        "angle":[30, 0, 0, 0, 0, 0, 0, 0],
        "walkemove": [0.1, 0, 0],
        "direction": 0
    }
}
```

| 参数        | 参数类型    | 说明               | 实例值                      |
| --------- | ------- | ---------------- | ------------------------ |
| angle     | float[] | 七个关节(弧度)+夹爪(角度)  | [0, 0, 0, 0, 0, 0, 0, 0] |
| walkemove | float[] | x(米), y(米)，角度(°) | [0, 0, 30]               |
| direction | int     | 方向               | [0, 3]取值，代表x正，x负、y正、y负   |
## 1.2 配置

**修改websocket的Ip和端口：**
> StreamingAssets\MyConfig\config.json文件中修改
## 1.3 交互

| 按键  | 效果  | 备注  |
| ------------ | ------------ | ------------ |
| tab  | 显示/隐藏快捷键提示 | 默认隐藏，打开显示所有快捷键  |
