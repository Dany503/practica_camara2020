from picamera import PiCamera
from time import sleep
#from gpiozero import Button
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # definimos la numeracion 
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP) # definimos el pin como salida
GPIO.setup(7,GPIO.OUT)
def espera_boton(pin):
    leeboton=GPIO.input(pin)
    while leeboton==1:
        leeboton=GPIO.input(pin)
        sleep(0.01)
    while leeboton==0:
        leeboton=GPIO.input(pin)
        sleep(0.01)

#button = Button(27)
camera = PiCamera()
camera.resolution = (640,480)
camera.rotation = 180
#camera.preview_fullscreen=False
camera.start_preview(fullscreen=False, window=(30,30,320,240))
#button.wait_for_press()
espera_boton(13)
camera.capture('prueba.jpg')
camera.stop_preview()
camera.close()

