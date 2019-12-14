#! /usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from ctrl_pkg.msg import ServoCtrlMsg

# this is called when gamepad key is pressed or joystick is moved
def joy_callback(data):
    	pub_manual_drive = rospy.Publisher('manual_drive', ServoCtrlMsg, queue_size=10)
   	msg = ServoCtrlMsg()
	msg.angle    = data.axes[3]
	msg.throttle = data.axes[4]
	rospy.loginfo('angle: %f ; throttle: %f' , msg.angle, msg.throttle)
	pub_manual_drive.publish(msg)


def joy_listener():
	# cntl is name of the node sent to ROS Master
	rospy.init_node('joy_cntl', anonymous=False)

	# subscribe to joystick messages on topic "joy"
	rospy.Subscriber("joy", Joy, joy_callback, queue_size=1)
	rospy.loginfo("Press CTRL+c to stop deepracer")
	rospy.spin()

if __name__ == '__main__':
    try:
        joy_listener()
    except rospy.ROSInterruptException:
        pass
