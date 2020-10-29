from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(30,30,320,240))
for i in range(1,4):
    print 4-i
    sleep(1)
camera.capture('/home/pi/imagen.jpg')
camera.stop_preview()
camera.close()

