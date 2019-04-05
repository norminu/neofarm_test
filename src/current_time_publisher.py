#!/usr/bin/env python

import rospy

from std_msgs.msg import String
from datetime import datetime

rospy.init_node('current_time_publisher')

pub = rospy.Publisher('current_time', String)

rate = rospy.Rate(0.1)

while not rospy.is_shutdown():
	ctime = datetime.now().strftime("%H:%M:%S")
	pub.publish(ctime)
	rate.sleep()
