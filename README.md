generating urdf from xacro

	rosrun xacro xacro panda.urdf.xacro > panda.urdf

Launching TCP endpoint

	roslaunch ros_tcp_endpoint endpoint.launch
	
Starting (custom) robot controller

	roslaunch franka_example_controllers cartesian_impedance_example_controller_edited.launch robot_ip:=172.16.0.2

Move home

	roslaunch franka_example_controllers move_to_start.launch robot_ip:=172.16.0.2

Gripper comms node
	rosrun comms_router pinch_gripper.py

# Touch AR

## Submodules
- Included ROS modules are tracked as git submodules.
  - add / commit / (pull) / push in submodule first

## Change force limits for the Panda
franka_ros/franka_control/config/franka_control_node.yaml
-> collsiion_config

## Switching controllers
Create a controller_groups.yaml file defining the groups
```yaml
controller_groups:
  joint_position:
    - franka_gripper
    - franka_state_controller
    - joint_position_example_controller
```
Load in launch file: (This registers the control groups in the master node and makes them available)
```
  <rosparam file="$(find franka_example_controllers)/config/_controller_groups.yaml" command="load" />
```
List current controllers:
```
rosrun controller_manager controller_manager list
```
Switch controllers with:
```
rosrun controller_manager controller_group switch joint_position
```