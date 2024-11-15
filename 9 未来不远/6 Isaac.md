```note
Joint 0 name: base_joint
Joint 1 name: rotate_base_joint
Joint 2 name: lifting_base_joint
Joint 3 name: gimbal_joint1
Joint 4 name: left_joint1
Joint 5 name: right_joint1
Joint 6 name: gimbal_joint2
Joint 7 name: left_joint2
Joint 8 name: right_joint2
Joint 9 name: gimbal_camera_joint
Joint 10 name: left_joint3
Joint 11 name: right_joint3
Joint 12 name: left_joint4
Joint 13 name: right_joint4
Joint 14 name: left_joint5
Joint 15 name: right_joint5
Joint 16 name: left_joint6
Joint 17 name: right_joint6
Joint 18 name: left_joint7
Joint 19 name: right_joint7
Joint 20 name: left_camera_base_joint
Joint 21 name: right_camera_base_joint
Joint 22 name: left_camera_joint
Joint 23 name: left_tool_base_joint
Joint 24 name: right_camera_joint
Joint 25 name: right_tool_base_joint
Joint 26 name: left_base_tool_joint
Joint 27 name: right_base_tool_joint
Joint 28 name: left_finger_joint1
Joint 29 name: left_finger_joint2
Joint 30 name: ll_tool_joint3
Joint 31 name: lr_tool_joint3
Joint 32 name: right_finger_joint1
Joint 33 name: right_finger_joint2
Joint 34 name: rl_tool_joint3
Joint 35 name: rr_tool_joint3
Joint 36 name: lr_tool_joint2
Joint 37 name: ll_tool_joint2
Joint 38 name: rr_tool_joint2
Joint 39 name: rl_tool_joint2
```

```shell
ros2 topic pub /joint_command sensor_msgs/JointState '{header: {stamp: {sec: 1720861606, nanosec: 489197117}, frame_id: ""}, name: ["right_joint1", "right_joint2", "right_joint3", "right_joint4", "right_joint5", "right_joint6", "right_joint7", "left_joint1", "left_joint2", "left_joint3", "left_joint4", "left_joint5", "left_joint6", "left_joint7"], position: [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}'
```