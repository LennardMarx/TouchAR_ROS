generating urdf from xacro

	rosrun xacro xacro panda.urdf.xacro > panda.urdf

Launching TCP endpoint

	roslaunch ros_tcp_endpoint endpoint.launch
	
Starting (custom) robot controller

	roslaunch franka_example_controllers cartesian_impedance_example_controller_edited.launch robot_ip:=172.16.0.2

Move home

	roslaunch franka_example_controllers move_to_start.launch robot_ip:=172.16.0.2

Calling Gripper Service

	rostopic pub /franka_gripper/move/goal franka_gripper/MoveActionGoal "header: 
	seq: 0
	stamp:
		secs: 0
		nsecs: 0
	frame_id: ''
	goal_id:
		stamp:
		secs:
		nsecs:
	id: ''
	goal:
		width: 0.02
		speed 0.1" 
		
Gripper comms node
	rosrun comms_router pinch_gripper.py
