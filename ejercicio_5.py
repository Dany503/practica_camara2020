# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 02:39:38 2016

@author: pi
"""

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()