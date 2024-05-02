#!/usr/bin/env python
import rospy
import actionlib
from std_msgs.msg import String
from std_msgs.msg import Float32
from franka_gripper.msg import MoveAction, MoveGoal

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    
    target_width = data.data
    target_speed = 0.1

    result = gripper_move_client(target_width, target_speed)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('pinch_listener', anonymous=True)
    #rospy.init_node('gripper_move_client')


    #rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("/custom_topics/pinch_distance", Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def gripper_move_client(width, speed):
    # Create a ROS action client for the MoveAction
    client = actionlib.SimpleActionClient('franka_gripper/move', MoveAction)

    # Wait for the action server to become available
    client.wait_for_server()

    # Create a goal to send to the action server
    goal = MoveGoal()
    goal.width = width
    goal.speed = speed

    # Send the goal to the action server and wait for result
    client.send_goal(goal)
    #client.wait_for_result()

    # Return the result of the action
    #return client.get_result()

if __name__ == '__main__':
    listener()

