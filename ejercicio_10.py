# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
camera.rotation = 180
camera.hflip = True
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(0.1)
print("Saca la primera foto pulsando a")
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
    image = frame.array
    #cv2.circle(image,(447,63), 63, (0,0,255), 5)
	# show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
 	# if the `q` key was pressed, break from the loop
    if key == ord("a"):
         #cv2.imwrite("afoto.jpg",image)
         imagen1=image
         cv2.imshow("A",imagen1)
         time.sleep(3)

         print("Saca la segunda foto pulsando B")
    if key == ord("b"):
         #cv2.imwrite("afoto.jpg",image)
         imagen2=image
         cv2.imshow("B",imagen2)
         time.sleep(3)

         print("Para mezclarlas, pulsa M")
         #break
    if key == ord("m"):
         alfa=input("mete porcentaje de mezcla")
         alfa_f=float(alfa)/100.0
         beta=1.0-alfa_f
         dst = cv2.addWeighted(imagen1,alfa_f,imagen2,beta,0)
         cv2.imshow("BLEND",dst)
         print "Mezcla al %s" %alfa
           
         time.sleep(3)
         print("Para salir, pulsa q")
    if key == ord("q"):
        break
         
         
camera.close()
cv2.destroyWindow("Frame")
