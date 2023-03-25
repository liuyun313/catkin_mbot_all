#!/usr/bin/env python
#coding=utf-8
import rospy
import math
#导入mgs到pkg中
from nav_msgs.msg import Odometry

#回调函数输入的应该是msg
def callback(Odometry):
    distance = math.sqrt(math.pow(Odometry.pose.pose.position.x, 2)+math.pow(Odometry.pose.pose.position.y, 2)) 
    rospy.loginfo('Distance from the original point=%f', distance)

def listener():
    rospy.init_node('pylistener', anonymous=True)
    #Subscriber函数第一个参数是topic的名称，第二个参数是接受的数据类型 第三个参数是回调函数的名称
    
    rospy.Subscriber('odom', Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

