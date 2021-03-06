from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# inicializa la cámara
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.rotation = 180
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(640, 480))

# espera un tiempo a aque la cámara esté lista
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # tomamos el array de numpy que reprsenta la image
    image = frame.array
	# muestra el frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
 
	# se pulsamos 'q' nos salimos del bucle
    if key == ord("q"):
         cv2.imwrite("/home/pi/foto.jpg",image) # guardamos la imagen
         break
camera.close()
cv2.destroyWindow("Frame")
