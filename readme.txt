docker images
docker ps

## Rebuild your Docker image:
docker build --no-cache -t ros-humble-doosan-final .

#manual gazebo install
apt remove -y gz-tools2
apt install -y ros-humble-gazebo-ros-pkgs ros-humble-gazebo-ros2-control


## commit to container:
docker commit ros_humble_doosan ros-humble-doosan-updated

## re-join container  
docker ps --format "{{.Names}}"

# (docker-in-docker in another terminal) docker exec -it dsr01_emulator bash

docker exec -it ros_humble_doosan_final bash

source /opt/ros/humble/setup.bash
source /ws_doosan/install/setup.bash


docker exec -it ros_humble_doosan_final bash
source /opt/ros/humble/setup.bash
source /ws_doosan/install/setup.bash

cd /ws_doosan && colcon build --symlink-install --packages-select doosan_m0609_moveit_control


#test env
ros2 launch doosan_m0609_moveit_control test_control.launch.py

ros2 service list | grep move_to


