#!/usr/bin/env python

import rospy
from neofarm_test.srv import TimePrinterService,TimePrinterServiceResponse

def print_time(request):
	print request.ctime
	return ""

rospy.init_node('time_printer_service')

service = rospy.Service('time_print', TimePrinterService, print_time)
rospy.spin()
