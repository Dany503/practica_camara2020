from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

def espera_boton(pin):
    leeboton=GPIO.input(pin)
    while leeboton==1:
        leeboton=GPIO.input(pin)
        sleep(0.01)
    while leeboton==0:
        leeboton=GPIO.input(pin)
        sleep(0.01)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeracion 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # definimos el pin como salida
camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
camera.start_preview(fullscreen=False, window=(30,30,320,240))

espera_boton(13)
camera.start_recording('/home/pi/video.mjpeg')
espera_boton(13)

camera.stop_recording()
camera.stop_preview()
camera.close()

