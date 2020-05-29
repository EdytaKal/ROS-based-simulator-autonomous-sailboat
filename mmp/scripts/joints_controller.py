#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

global wind_dir 

def adjust_sail(wind):

	wind_dir = wind.data
	position_msg =  Float64()
        #Transferring values from a range of a sail (from 0 to 2.0) to the range of wind direction
        #-1/2 * 2/90 * wind_dir = -0.5 * 0.02222222222 * wind_dir
        position_msg.data = -0.01* wind_dir
	#Create the publisher to the sail controller topic.
	sail_pub = rospy.Publisher('/boat/sail_controller/command', Float64, queue_size=10)
	sail_pub.publish(position_msg.data)
	#Create the publisher to the rudder controller topic.
	rudder_pub = rospy.Publisher('/boat/rudder_controller/command', Float64, queue_size=10)
	rudder_pub.publish(position_msg.data*-1)
	
	#Print for debugging purposes. Comment out when not needed.
	#rospy.loginfo("Wind: %s", wind_dir)
	#print(position_msg.data)

def listener_new():
	
	rospy.init_node("listener", anonymous=True)
	rospy.Subscriber('/mmp_wind_topic/direction', Float64, adjust_sail)
	rospy.spin()

if __name__ == '__main__':
	
	try:
		listener_new()
	except rospy.ROSInterruptException:
		pass
