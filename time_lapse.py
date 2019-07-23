import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time


# Enter the path where the raspberry pi will store its file
RASPI_PATH = ""

INTERVAL = 2# the time interval (in seconds) between pictures
SESSION_LENGTH = 600# the duration of the script

camera = PiCamera(resolution = (1280, 720), framerate = 30)
camera.iso = 100
sleep(2)
#camera.shutter_speed = camera.exposure_speed
#camera.exposure_mode = 'off'
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g

#camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])
for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    sleep(5) # wait 5 seconds


# Have the camera take pictures at the specified interval until the session is over


