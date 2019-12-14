# AWS-Deepracer-Gamepad-Control
Control the AWS Deepracer directly with a Logitech F710 PS3 gamepad
## Overview
The AWS Deepracer can be operated using the virtual joystick on the web interface but the lag in response time is horrendous.  I recommend bypassing the web interface and controlling the racer directly and remotely with a gamepad.  You can even watch the video stream from the front mounted camera while using the gamepad.  It is not difficult to get up and running.

## Details
This repository will add two ROS nodes to control the AWS Deepracer directly using the Logitech F710 Gamepad thereby bypassing the web interface control.

The AWS Deepracer can be powered up directly by using the same USB-C power adapter that is used to charge the computer battery.  The HDMI connector is full size but the USB is a micro port so an [adapter](https://www.amazon.com/gp/product/B01HYJLZH6) must be used to connect a USB mouse, keyboard, and gamepad dongle.

This setup uses the [Logitech F710 Gamepad](https://www.amazon.com/Logitech-940-000117-Gamepad-F710/dp/B0041RR0TW).  This gamepad is rock solid and requires no bluetooth setup.  Just plug the included gamepad dongle and go.  It also works great with the Raspberry Pi.  It appears that the deepracer has no bluetooth which is another reason to use this gamepad.

Pre-installed AWS startup files load ROS components at boot time.  This setup does not mess with the pre-installed components, it only adds additional ROS nodes.  Not all of the original ROS nodes are used so you may eventually want to comment out unessential nodes in the file "/opt/aws/deepracer/share/deepracer_launcher/launch/deepracer.launch".

## Installation
Install the ROS joystick package.
```
sudo apt-get install ros-kinetic-joy
```
Follow the instructions in section ["Configuring the Joystick"](http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick) to verify the joystick is working and accessible.

If you have not already created a catkin workspace in your home directory you can follow the [instructions](http://wiki.ros.org/ROS/Tutorials/BuildingPackages) to create one.  Navigate to the src directory.
```
cd ~/catkin_ws/src
https://github.com/cmasenas/AWS-Deepracer-Gamepad-Control.git
```
## Starting the ROS gamepad control
To start the ROS nodes "joy" and "joy_cntl" navigate to the launch directory and use the launch file.
```
cd ~/catkin_ws/src/deepracer_cntl/launch
roslaunch deepracer_cntl joy_cntl.launch
```
All of the AWS pre-installed ROS code loads at boot time so starting the joy_cntl launcher is the only thing necessary once the installation is done.

## Driving Untethered
You can drive the deepracer remotely using only the gamepad or you can also view the camera feed on a network connected computer. 
The deepracer hostname can be found on the underside of the deepracer.
```
ssh deepracer@HOSTNAME.local
cd ~/catkin_ws/src/deepracer_cntl/launch
roslaunch deepracer_cntl joy_cntl.launch
```
To view the camera feed the firewall must first be stopped.
```
sudo ufw disable
```
Then the video stream can be viewed in a web browser.

```
http://HOSTNAME.local:8080/stream_viewer?topic=/video_mjpeg
```



