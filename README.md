# ROS-based-simulator-autonomous-sailboat
This project focuses on the development of the simulator of the autonomous sailing boat in the Robot Operating System (ROS). It consists of the control mechanism for the boat, which enables the vessel to travel without any input from the user apart from the designated direction of sailing. The sailboat adapts the sail and rudder positions depending on the chosen trajectory.

# List of the used tools.

•	Ubuntu 18.04

•	ROS melodic

•	RViz

•	Gazebo

•	Virtual RobotX Gazebo Simulator
 
# Instructions for installing the VRX Gazebo Simulator.

To install the Virtual RobotX Simulator follow the instructions from the following website:
https://bitbucket.org/osrf/vrx/wiki/tutorials/SystemSetupInstall

# Operator’s manual for the simulator.
 
This simulator has been developed and tested on the machine with the Ubuntu 18.4 and ROS melodic installed. To run the simulator it is also required to have the VRX simulation downloaded.

The next step is to create and build a catkin workspace, which has been explained in the following tutorial: http://wiki.ros.org/catkin/Tutorials/create_a_workspace. After this is completed the terminal should be opened and the successive command should be run:
$ cd catkin_ws/src

The mmp package with the simulator code should be installed in the abovementioned location.

In the new terminal window run roscore to enable communication between ROS nodes:
$ roscore

It is necessary to source the setup.*sh file in each newly opened terminal window:
$ cd catkin_ws
$ source devel/setup.bash

In the new terminal start the simulator, by launching the gazebo.launch file $ roslaunch mmp gazebo.launch

To start wind and GPS topics input the following commands in separate terminal windows:
$ rosrun mmp mmp_wind_topic.py

And

$ mmp_gps_topic.py

In order to display the GPS reading run the following:
$ rosrun pub_boat_pos.py

Necessary for starting the movement of the sail and rudder is running the successive command:

$ rosrun mmp joints_controller.py

Finally to start the boat sailing towards the waypoint behaviour run:
$ rosrun change_pose.py

In order to change the coordinates of the waypoint the waypoint_x and waypoint_y variables in the change_pos.py file has to be changed.
 
