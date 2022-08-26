# Image conversion for RobotX camera
## Installation 
This code was working with ROS2 Galactic.
It has dependency
- cv_bridge
- opencv
- message_filters
- rclpy

Run ```calcon build --packcage-select image_reader``` to build the package and ```source install/setup.bash``` to source, ***don't for get to change the image save to path in the code. Please change topic names accordingly***. 

## Run
Before running any rosbag, Please make sure the image_reader_node subscribed to the throttled topic declared in throttle.sh. To run the code first
```
sudo chmod +x throttle.sh
./throttle.sh
```
Two terminal window will popup and topic will be throttled. Then
```
ros2 run image_reader converter
```
and play ros bag
```
ros2 bag paly "bag-name"
```
