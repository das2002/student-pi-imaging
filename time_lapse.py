import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time
import picamera
import numpy as np
import cv2

RASPI_PATH = "/home/pi/"
INTERVAL = 2# the time interval (in seconds) between pictures
SESSION_LENGTH = 600# the duration of the script

with picamera.PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    image = np.empty((240 * 320 * 3,), dtype=np.uint8)
    for filename in camera.capture_continuous(RASPI_PATH + 'img{counter:03d}.bgr''):
        print('Captured %s' % filename)
        sleep(INTERVAL) # wait 5 seconds
    #camera.capture(image, 'bgr')
        image = image.reshape((240, 320, 3))

# Enter the path where the raspberry pi will store its file


#camera = PiCamera(resolution = (1280, 720), framerate = 30)
#camera.iso = 100
#sleep(2)
#camera.shutter_speed = camera.exposure_speed
#camera.exposure_mode = 'off'
#g = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = g

#camera.capture_sequence(['image%02d.jpg' % i for i in range(10)])



# Have the camera take pictures at the specified interval until the session is over


