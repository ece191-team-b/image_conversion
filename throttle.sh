#!/bin/bash

echo Starting throttling image 

gnome-terminal -- /usr/bin/bash -c 'ros2 run topic_tools throttle messages camera/image_0 0.5 /camera/throttle/image_0'
gnome-terminal -- /usr/bin/bash -c 'ros2 run topic_tools throttle messages camera/image_1 0.5 /camera/throttle/image_1'

