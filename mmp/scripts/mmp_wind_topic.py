#! /usr/bin/env python

import rospy 
from std_msgs.msg import Float64

#Crete the new topic for wind parameters.
rospy.init_node("wind_topic")
#Create the publisher to the wind direction topic.
direction_pub = rospy.Publisher('/mmp_wind_topic/direction', Float64, queue_size=10)
direction_msg = Float64()
direction_msg.data = -90.0
#Create the publisher to the wind speed topic.
speed_pub = rospy.Publisher('/mmp_wind_topic/speed', Float64, queue_size=10)
speed_msg = Float64()
speed_msg.data = 20.0

while not rospy.is_shutdown():
	#The wind values can varies from -90 to 90.
	for direction_msg.data in range(-90,90):
		#Publish the messages to the wind speed and direction topics.
                direction_pub.publish(direction_msg)
                speed_pub.publish(speed_msg)
                direction_msg.data += 1.0
                #Print for debugging purposes. Comment out when not needed.
		#print(direction_msg.data)
                rospy.sleep(1)



