from picamera import PiCamera
from time import sleep
#from gpiozero import Button
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeracion 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # definimos el pin como salida
GPIO.setup(7,GPIO.OUT)
#button = Button(27)
camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
#camera.preview_fullscreen=False
camera.start_preview(fullscreen=False, window=(30,30,320,240))
#button.wait_for_press()
leeboton=GPIO.input(13)
while leeboton==1:
    leeboton=GPIO.input(13)
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    camera.capture('/home/pi/imagen_%s.jpg' % effect)
camera.stop_preview()
camera.close()

