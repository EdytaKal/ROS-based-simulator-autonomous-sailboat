#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState, GetModelState, GetModelStateRequest
from tf.transformations import euler_from_quaternion
from math import atan2

global pose_x
global pose_y
global yaw
global waypoint_x
global waypoint_y

def callback(msg):
	pub_odom = rospy.Publisher('/boat/odom', Odometry, queue_size = 10)
	pose_x = msg.pose.pose.position.x
	pose_y = msg.pose.pose.position.y
	state_msg = ModelState()
        state_msg.model_name = 'sailboat'
	
	#Caclulate pitch, yaw and roll values from the orientation numbers to determine the direction the boat is facing.	
	orientation_q = msg.pose.pose.orientation
	orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
	(roll, pitch, yaw) = euler_from_quaternion(orientation_list)
	print 'x:', pose_x
	print 'y:', pose_y
	print '------------'
	print 'yaw:', yaw
	print '------------'
	
	#Caclulating how much the boat has to turn to face the direction of waypoint.
	inc_x = waypoint_x - pose_x
	inc_y = waypoint_y - pose_y
	angle_to_goal = atan2(inc_y, inc_x)
	print inc_x, inc_y, angle_to_goal
	#If the boat is facing the wrong way, rotate it until it is positioned in the direction of the waypoint otherwise print the message.
	if abs(angle_to_goal - yaw)>0.1:
        	state_msg.pose.position.x = pose_x + 0.3 
        	#pub_odom.publish(pose_z + 0.3)
		rospy.wait_for_service('/gazebo/get_model_state')
		set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
		resp = set_state(state_msg)
	else:
		print ('Boat faces the waypoint')

waypoint_x = 5.0
waypoint_y = 5.0
rospy.init_node('odom_subscriber')
sub_odom = rospy.Subscriber('/boat/odom', Odometry, callback)
rospy.spin()
