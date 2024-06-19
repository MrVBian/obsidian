https://blog.csdn.net/joyopirate/article/details/129046318
# Overview

This pages describes the changes for the camera plugins in `gazebo_plugins` for ROS2, including a guide to migrate.

# Table of Contents
1. [Deprecation of gazebo_ros_camera_utils](#gazebo_ros_camera_utils)
1. [Shared Migration Steps](#Shared)
    1. [SDF Parameters](#sdf_parameters)
1. [Additional steps for gazebo_ros_camera](#gazebo_ros_camera)
1. [Additional steps for gazebo_ros_triggered_camera](#gazebo_ros_triggered_camera)
1. [Additional steps for gazebo_ros_multicamera](#gazebo_ros_multicamera)
1. [Additional steps for gazebo_ros_triggered_multicamera](#gazebo_ros_triggered_multicamera)
1. [Additional steps for gazebo_ros_depth_camera](#gazebo_ros_depth_camera)
1. [Additional steps for gazebo_ros_openni_kinect](#gazebo_ros_openni_kinect)
1. [gazebo_ros_prosilica](#gazebo_ros_prosilica)

## gazebo_ros_camera_utils

On ROS 1, this file provided the class `GazeboRosCameraUtils`, which served as a base class for several plugins. On ROS 2, the functionality which used to be provided by this class is now provided directly by `gazebo_ros_camera`, which can be configured via SDF to behave like the plugins which used to depend on camera utils.

Some of the problems with the ROS 1 approach were:

1. Plugins had multiple inheritance, from `GazeboRosCameraUtils` and `CameraPlugin`, and had to copy inherited variables like `parentSensor` between these classes.

1. `GazeboRosCameraUtils`, instead of being a thin base class which only provided functionality which is common among plugins, would also provide features that some inherited classes wouldn't use, like triggering. So we might as well expose this functionality in a single plugin and reduce code duplication.

## Shared

* **Topic names**: they should be given by remapping arguments inside `<ros>`, so `<imageTopicName>` and `<cameraInfoTopicName>` are deprecated.

* **Distortion**: On ROS1, distortion had to either be:
    * duplicated between the camera sensor and the plugin
    * or the `<auto_distortion>` flag had to be set to true so the plugin would use the distortion from the sensor

    On ROS2, all these flags are deprecated, and the distortion from the camera is always used.

* **Update rate**: set the rate on the sensor.

* **TF Frame ID**: The use of tf prefixes has been [deprecated entirely](http://wiki.ros.org/tf2/Migration#Removal_of_support_for_tf_prefix). The TF frame will by default be the name of the link the sensor is attached to, but may be overridden by setting the ```<frame_name>``` tag.

* **Namespaces**: ROS 1 used a combination of 2 tags to set the node's namespace: ```<robotNamespace>```/`<cameraName>`. On ROS 2, the namespace is [given by](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-integration#open_file_folder-gazebo_ros) ```<ros><namespace>my_namespace</namespace></ros>``` and `<camera_name>` is prepended to all the advertized topics, but is not part of the namespace.

### SDF parameters

| ROS 1 | ROS 2 |
| ----- | ----- |
| `imageTopicName` | `<ros><remapping>image_raw:=custom_image_raw</remapping></ros>` |
| `cameraInfoTopicName` | `<ros><remapping>camera_info:=custom_camera_info</remapping></ros>` |
| `robotNamespace` | ```<ros><namespace>my_namespace</namespace></ros>``` |
| `cameraName` | `camera_name` |
| `frameName` | `frame_name` |
| `hackBaseline` | `hack_baseline` |
| `autoDistortion` | :x: |
| `distortionK1` | :x: |
| `distortionK2` | :x: |
| `distortionK3` | :x: |
| `distortionT1` | :x: |
| `distortionT2` | :x: |
| `updateRate` | :x: |

## gazebo_ros_camera

No additional changes.

### Example Migration

# ROS1
```.xml
  <link name="link_name">
    ...
    <sensor type="camera" name="sensor_name">
      ...
      <always_on>0</always_on>
      <update_rate>1</update_rate>

      <camera name="camera_name">
        ...
        <distortion>
          <k1>0.1</k1>
          <k2>0.2</k2>
          <k3>0.3</k3>
          <p1>0.4</p1>
          <p2>0.5</p2>
          <center>0.5 0.5</center>
        </distortion>
      </camera>

      <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>0.0</updateRate>
        <robotNamespace>custom_ns</robotNamespace>
        <cameraName>custom_camera</cameraName>
        <imageTopicName>custom_image</imageTopicName>
        <cameraInfoTopicName>custom_info</cameraInfoTopicName>
        <frameName>custom_frame</frameName>
        <hackBaseline>0.07</hackBaseline>
        <distortionK1>0.1</distortionK1>
        <distortionK2>0.2</distortionK2>
        <distortionK3>0.3</distortionK3>
        <distortionT1>0.5</distortionT1>
        <distortionT2>0.5</distortionT2>
      </plugin>
    </sensor>
  </link>
```

# ROS2
```.xml
      <link name="link_name">
        ...
        <sensor type="camera" name="sensor_name">
          ...

          <!-- Set always_on only sensor, not on plugin -->
          <always_on>0</always_on>

          <!-- Set update_rate only sensor, not on plugin -->
          <update_rate>1</update_rate>

          <camera name="camera_name">
            ...
            <distortion>
              <k1>0.1</k1>
              <k2>0.2</k2>
              <k3>0.3</k3>
              <p1>0.4</p1>
              <p2>0.5</p2>
              <center>0.5 0.5</center>
            </distortion>
          </camera>

          <!-- Use camera, not camera_triggered -->
          <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
            <!-- Change namespace, camera name and topics so -
                 * Images are published to: /custom_ns/custom_camera/custom_image
                 * Camera info is published to: /custom_ns/custom_camera/custom_info
            -->
            <ros>
              <namespace>custom_ns</namespace>
              <remapping>image_raw:=custom_img</remapping>
              <remapping>camera_info:=custom_info</remapping>
            </ros>

            <!-- Set camera name. If empty, defaults to sensor name (i.e. "sensor_name") -->
            <camera_name>custom_camera</camera_name>

            <!-- Set TF frame name. If empty, defaults to link name (i.e. "link_name") -->
            <frame_name>custom_frame</frame_name>

            <hack_baseline>0.07</hack_baseline>

            <!-- No need to repeat distortion parameters or to set autoDistortion -->
          </plugin>
        </sensor>
```

## gazebo_ros_triggered_camera

### Additional changes:

* Instead of using a different plugin, use `gazebo_ros_camera` and pass the `<triggered>true</triggered>` flag.
* The trigger topic can be changed by remapping: `<ros><remapping>image_trigger:=image_trigger_test</remapping></ros>`

### Example Migration

# ROS1
```.xml
  <link name="link_name">
    ...
    <sensor type="camera" name="sensor_name">
      ...
      <always_on>0</always_on>
      <update_rate>1</update_rate>

      <camera name="camera_name">
        ...
        <distortion>
          <k1>0.1</k1>
          <k2>0.2</k2>
          <k3>0.3</k3>
          <p1>0.4</p1>
          <p2>0.5</p2>
          <center>0.5 0.5</center>
        </distortion>
      </camera>

      <plugin name="plugin_name" filename="libgazebo_ros_triggered_camera.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>0.0</updateRate>
        <robotNamespace>custom_ns</robotNamespace>
        <triggerTopicName>custom_trigger</triggerTopicName>
        <cameraName>custom_camera</cameraName>
        <imageTopicName>custom_image</imageTopicName>
        <cameraInfoTopicName>custom_info</cameraInfoTopicName>
        <frameName>custom_frame</frameName>
        <hackBaseline>0.07</hackBaseline>
        <distortionK1>0.1</distortionK1>
        <distortionK2>0.2</distortionK2>
        <distortionK3>0.3</distortionK3>
        <distortionT1>0.5</distortionT1>
        <distortionT2>0.5</distortionT2>
      </plugin>
    </sensor>
  </link>
```

# ROS2
```.xml
      <link name="link_name">
        ...
        <sensor type="camera" name="sensor_name">
          ...

          <!-- Set always_on only sensor, not on plugin -->
          <always_on>0</always_on>

          <!-- Set update_rate only sensor, not on plugin -->
          <update_rate>1</update_rate>

          <camera name="camera_name">
            ...
            <distortion>
              <k1>0.1</k1>
              <k2>0.2</k2>
              <k3>0.3</k3>
              <p1>0.4</p1>
              <p2>0.5</p2>
              <center>0.5 0.5</center>
            </distortion>
          </camera>

          <!-- Use camera, not camera_triggered -->
          <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
            <!-- Change namespace, camera name and topics so -
                 * Images are published to: /custom_ns/custom_camera/custom_image
                 * Camera info is published to: /custom_ns/custom_camera/custom_info
                 * Trigger is received on: /custom_ns/custom_camera/custom_trigger
            -->
            <ros>
              <namespace>custom_ns</namespace>
              <remapping>image_raw:=custom_img</remapping>
              <remapping>camera_info:=custom_info</remapping>
              <remapping>image_trigger:=custom_trigger</remapping>
            </ros>

            <!-- Set camera name. If empty, defaults to sensor name (i.e. "sensor_name") -->
            <camera_name>custom_camera</camera_name>

            <!-- Set TF frame name. If empty, defaults to link name (i.e. "link_name") -->
            <frame_name>custom_frame</frame_name>

            <!-- Set to true to turn on triggering -->
            <triggered>true</triggered>

            <hack_baseline>0.07</hack_baseline>

            <!-- No need to repeat distortion parameters or to set autoDistortion -->
          </plugin>
        </sensor>
```

## gazebo_ros_multicamera

### Additional changes:
* Instead of using a different plugin, use gazebo_ros_camera.
* Multi camera is no longer limited to 2 cameras as in ROS1.
* Topic names: they should be given by remapping arguments inside `<ros>`.
* The image topic name by default is as follows: /namespace/camera_name(common)/camera(individual)/image_raw
* The camera info topic name by default is as follows: /namespace/camera_name(common)/camera(individual)/camera_info

### SDF parameters

| ROS 1 | ROS 2 |
| ----- | ----- |
| `imageTopicName` | `<ros><remapping>custom_cam/cam_name/image_raw:=custom_image_raw</remapping></ros>` |
| `cameraInfoTopicName` | `<ros><remapping>custom_cam/cam_name/camera_info_:=custom_camera_info</remapping></ros>` |

### Example Migration

# ROS1
```.xml
  <link name="link_name">
    ...
    <sensor type="multicamera" name="stereo_camera">
      <update_rate>30.0</update_rate>
      <camera name="left">
        ...
      </camera>
      <camera name="right">
        ...
      </camera>
      <plugin name="stereo_camera_controller" filename="libgazebo_ros_multicamera.so">
        <alwaysOn>true</alwaysOn>
        <updateRate>0.0</updateRate>
        <cameraName>multisense_sl/camera</cameraName>
        <imageTopicName>image_raw</imageTopicName>
        <cameraInfoTopicName>camera_info</cameraInfoTopicName>
        <frameName>left_camera_optical_frame</frameName>
      </plugin>
    </sensor>
  </link>
```

# ROS2
```.xml
      <link name="link_name">

        <sensor type="multicamera" name="sensor_name">
          <camera name="left">
            ...
          </camera>
          <camera name="right">
            ...
          </camera>

          <!-- Set update_rate only sensor, not on plugin -->
          <update_rate>1</update_rate>

          <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
            <!-- Change namespace, camera name and topics so -
                 * Left images are published to: /custom_ns/custom_camera/left/custom_image
                 * Right images are published to: /custom_ns/custom_camera/right/custom_image
                 * Left camera info is published to: /custom_ns/custom_camera/left/custom_camera_info
                 * Right camera info is published to: /custom_ns/custom_camera/right/custom_camera_info
            -->
            <ros>
              <namespace>custom_ns</namespace>
              <!-- topics need to be prefixed with camera_name for remapping -->
              <remapping>custom_camera/left/image_raw:=custom_camera/left/custom_image</remapping>
              <remapping>custom_camera/right/image_raw:=custom_camera/right/custom_image</remapping>
              <remapping>custom_camera/left/camera_info:=custom_camera/left/custom_camera_info</remapping>
              <remapping>custom_camera/right/camera_info:=custom_camera/right/custom_camera_info</remapping>
            </ros>

            <camera_name>custom_camera</camera_name>

            <frame_name>left_camera_optical_frame</frameName>
          </plugin>
        </sensor>
```

## gazebo_ros_triggered_multicamera

### Additional changes:
* Instead of using a different plugin, use `gazebo_ros_camera` as [gazebo_ros_multicamera](#gazebo_ros_multicamera) and pass `<triggered>true</triggered>` flag.
* The trigger topic can be changed by remapping: `<ros><remapping>image_trigger:=image_trigger_test</remapping></ros>`

## gazebo_ros_depth_camera

### Additional changes:
* Instead of using a different plugin, use `gazebo_ros_camera`.
* **Topic names**: they should be given by remapping arguments inside `<ros>`, so `<depthImageTopicName>`, `<depthImageCameraInfoTopicName` and `<pointCloudTopicName>` are deprecated.

### SDF parameters

| ROS 1 | ROS 2 |
| ----- | ----- |
| `depthImageTopicName` | `<ros><remapping>custom_cam/image_depth:=custom_depth_raw</remapping></ros>` |
| `depthImageCameraInfoTopicName` | `<ros><remapping>custom_cam/camera_info_depth:=custom_camera_info</remapping></ros>` |
| `pointCloudTopicName` | `<ros><remapping>custom_cam/points:=custom_points</remapping></ros>` |
| `pointCloudCutoff` | `min_depth` |

### Example Migration

# ROS1
```.xml
  <link name="link_name">
    ...
    <sensor type="depth" name="sensor_name">
      ...
      <always_on>0</always_on>
      <update_rate>1</update_rate>

      <camera name="camera_name">
        ...
        <distortion>
          <k1>0.1</k1>
          <k2>0.2</k2>
          <k3>0.3</k3>
          <p1>0.4</p1>
          <p2>0.5</p2>
          <center>0.5 0.5</center>
        </distortion>
      </camera>

      <plugin name="camera_controller" filename="libgazebo_ros_depth_camera.so">
        <alwaysOn>true</alwaysOn>
        <!-- Keep this zero, update_rate will control the frame rate -->
        <updateRate>0.0</updateRate>
        <cameraName>camera1</cameraName>
        <imageTopicName>custom_image</imageTopicName>
        <cameraInfoTopicName>custom_info_raw</cameraInfoTopicName>
        <depthImageTopicName>custom_image_depth</depthImageTopicName>
        <depthImageCameraInfoTopicName>custom_info_depth</depthImageCameraInfoTopicName>
        <pointCloudTopicName>custom_points</pointCloudTopicName>
        <frameName>camera_link</frameName>

        <pointCloudCutoff>0.001</pointCloudCutoff>
        <hackBaseline>0.07</hackBaseline>
        <distortionK1>0.0</distortionK1>
        <distortionK2>0.0</distortionK2>
        <distortionK3>0.0</distortionK3>
        <distortionT1>0.0</distortionT1>
        <distortionT2>0.0</distortionT2>
      </plugin>
    </sensor>
  </link>
```

# ROS2
```.xml
      <link name="link_name">
        ...
        <sensor type="depth" name="sensor_name">
          ...

          <!-- Set always_on only sensor, not on plugin -->
          <always_on>0</always_on>

          <!-- Set update_rate only sensor, not on plugin -->
          <update_rate>1</update_rate>

          <camera name="camera_name">
            ...
            <distortion>
              <k1>0.1</k1>
              <k2>0.2</k2>
              <k3>0.3</k3>
              <p1>0.4</p1>
              <p2>0.5</p2>
              <center>0.5 0.5</center>
            </distortion>
          </camera>

          <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
            <!-- Change namespace, camera name and topics so -
                 * Raw images are published to: /custom_ns/custom_camera/custom_image
                 * Depth images are published to: /custom_ns/custom_camera/custom_image_depth
                 * Raw image camera info is published to: /custom_ns/custom_camera/custom_info_raw
                 * Depth image camera info is published to: /custom_ns/custom_camera/custom_info_depth
                 * Point cloud is published to: /custom_ns/custom_camera/custom_points
            -->
            <ros>
              <namespace>custom_ns</namespace>
              <remapping>custom_camera/image_raw:=custom_camera/custom_image</remapping>
              <remapping>custom_camera/image_depth:=custom_camera/custom_image_depth</remapping>
              <remapping>custom_camera/camera_info:=custom_camera/custom_info_raw</remapping>
              <remapping>custom_camera/camera_info_depth:=custom_camera/custom_info_depth</remapping>
              <remapping>custom_camera/points:=custom_camera/custom_points</remapping>
            </ros>

            <!-- Set camera name. If empty, defaults to sensor name (i.e. "sensor_name") -->
            <camera_name>custom_camera</camera_name>

            <!-- Set TF frame name. If empty, defaults to link name (i.e. "link_name") -->
            <frame_name>custom_frame</frame_name>

            <hack_baseline>0.07</hack_baseline>

            <!-- No need to repeat distortion parameters or to set autoDistortion -->

             <min_depth>0.001</min_depth>
          </plugin>
        </sensor>
```

## gazebo_ros_openni_kinect

### Additional changes:

* Instead of using a different plugin, use `gazebo_ros_camera`.

### SDF parameters

| ROS 1 | ROS 2 |
| ----- | ----- |
| `pointCloudCutoffMax` | `max_depth` |

### Example Migration

# ROS1
```.xml
  <link name="link_name">
    ...
    <sensor type="depth" name="sensor_name">
      ...
      <always_on>0</always_on>
      <update_rate>1</update_rate>

      <camera name="camera_name">
        ...
        <distortion>
          <k1>0.1</k1>
          <k2>0.2</k2>
          <k3>0.3</k3>
          <p1>0.4</p1>
          <p2>0.5</p2>
          <center>0.5 0.5</center>
        </distortion>
      </camera>

      <plugin name="camera_controller" filename="libgazebo_ros_openni_kinect.so">
        <alwaysOn>true</alwaysOn>
        <!-- Keep this zero, update_rate will control the frame rate -->
        <updateRate>0.0</updateRate>
        <cameraName>camera1</cameraName>
        <imageTopicName>custom_image</imageTopicName>
        <cameraInfoTopicName>custom_info_raw</cameraInfoTopicName>
        <depthImageTopicName>custom_image_depth</depthImageTopicName>
        <depthImageCameraInfoTopicName>custom_info_depth</depthImageCameraInfoTopicName>
        <pointCloudTopicName>custom_points</pointCloudTopicName>
        <frameName>camera_link</frameName>

        <pointCloudCutoff>0.001</pointCloudCutoff>
        <pointCloudCutoffMax>300.0</pointCloudCutoffMax>
        <hackBaseline>0.07</hackBaseline>
        <distortionK1>0.0</distortionK1>
        <distortionK2>0.0</distortionK2>
        <distortionK3>0.0</distortionK3>
        <distortionT1>0.0</distortionT1>
        <distortionT2>0.0</distortionT2>
      </plugin>
    </sensor>
  </link>
```

# ROS2
```.xml
      <link name="link_name">
        ...
        <sensor type="depth" name="sensor_name">
          ...

          <!-- Set always_on only sensor, not on plugin -->
          <always_on>0</always_on>

          <!-- Set update_rate only sensor, not on plugin -->
          <update_rate>1</update_rate>

          <camera name="camera_name">
            ...
            <distortion>
              <k1>0.1</k1>
              <k2>0.2</k2>
              <k3>0.3</k3>
              <p1>0.4</p1>
              <p2>0.5</p2>
              <center>0.5 0.5</center>
            </distortion>
          </camera>

          <plugin name="plugin_name" filename="libgazebo_ros_camera.so">
            <!-- Change namespace, camera name and topics so -
                 * Raw images are published to: /custom_ns/custom_camera/custom_image
                 * Depth images are published to: /custom_ns/custom_camera/custom_image_depth
                 * Raw image camera info is published to: /custom_ns/custom_camera/custom_info_raw
                 * Depth image camera info is published to: /custom_ns/custom_camera/custom_info_depth
                 * Point cloud is published to: /custom_ns/custom_camera/custom_points
            -->
            <ros>
              <namespace>custom_ns</namespace>
              <remapping>custom_camera/image_raw:=custom_camera/custom_image</remapping>
              <remapping>custom_camera/image_depth:=custom_camera/custom_image_depth</remapping>
              <remapping>custom_camera/camera_info:=custom_camera/custom_info_raw</remapping>
              <remapping>custom_camera/camera_info_depth:=custom_camera/custom_info_depth</remapping>
              <remapping>custom_camera/points:=custom_camera/custom_points</remapping>
            </ros>

            <!-- Set camera name. If empty, defaults to sensor name (i.e. "sensor_name") -->
            <camera_name>custom_camera</camera_name>

            <!-- Set TF frame name. If empty, defaults to link name (i.e. "link_name") -->
            <frame_name>custom_frame</frame_name>

            <hack_baseline>0.07</hack_baseline>

            <!-- No need to repeat distortion parameters or to set autoDistortion -->

             <min_depth>0.001</min_depth>
             <max_depth>300.0</max_depth>
          </plugin>
        </sensor>
```
## gazebo_ros_prosilica
:warning:  deprecated