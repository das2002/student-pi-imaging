import os
import datetime
from datetime import tzinfo
import math
from picamera import PiCamera
from time import sleep
import time


# Enter the path where the raspberry pi will store its file
RASPI_PATH = ""

INTERVAL = None# the time interval (in seconds) between pictures
SESSION_LENGTH = None# the duration of the script

camera = PiCamera()
camera.start_preview()


# Have the camera take pictures at the specified interval until the session is over


camera.stop_preview()

