#! /usr/bin/env python
# based on code from: https://answers.ros.org/question/222033/how-do-i-publish-gazebo-position-of-a-robot-model-on-odometry-topic/

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import Header
from gazebo_msgs.srv import GetModelState, GetModelStateRequest

if __name__ == '__main__':
	#Create the odom_pub node.
	rospy.init_node('odom_pub')
	#Create the publisher to the /boat/odom topic.
	odom_pub=rospy.Publisher ('/boat/odom', Odometry, queue_size=10) 
	rospy.wait_for_service ('/gazebo/get_model_state')
	get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

	odom=Odometry()
	header = Header()
	header.frame_id='boat/odom' 

	model = GetModelStateRequest()
	model.model_name='sailboat'

	r = rospy.Rate(2)

	while not rospy.is_shutdown():
	    result = get_model_srv(model)
	    #Assign the received values from the Gazebo to the odometry topic.
	    odom.pose.pose = result.pose
	    odom.twist.twist = result.twist

	    header.stamp = rospy.Time.now()
	    odom.header = header
	    #Publish the received values to the odometry topic.
	    odom_pub.publish (odom)

	    r.sleep()
