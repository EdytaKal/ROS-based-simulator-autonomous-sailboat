#! /usr/bin/env python

import rospy 
from nav_msgs.msg import Odometry
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

global boat_odom_list

def get_odom(odom):
	#Create the list for the x and y coordinates of the boat position in the Gazebo.
	boat_odom_list = odom.pose.pose.position.x, odom.pose.pose.position.y
	print boat_odom_list

def main():
	#Create the new node.
	rospy.init_node('movement', anonymous=True)
	#Create the subscriber to the /boat/odom topic.
	rospy.Subscriber('/boat/odom', Odometry, get_odom)
	rospy.spin()

if __name__=="__main__":
	main()
