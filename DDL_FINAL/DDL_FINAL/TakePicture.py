


#DDL Project December 13th 2018
#Author: Kevin Lee, Jean-Christophe Owens
#GPIO, OPENCV


from PIL import Image
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import cv2
import numpy as np
from function_library import *

opt_parse()
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


def TakePicture():
    camera = PiCamera()

    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Desktop/DDL/Image.jpg', resize=(684, 486))
    camera.stop_preview()



def OpenCVTest():

    image = cv2.imread("/home/pi/Desktop/DDL/Image.jpg")

    #Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    #define color strength parameters in HSV
    #Green
    weaker = np.array([65,60,60])
    stronger = np.array([80,255,255])

    #BLUE
    #weaker = np.array([60,100,100])
    #stronger = np.array([180,255,255])

    #RED
    #weaker = np.array([0,50,50])
    #stronger = np.array([10,255,255])

    #Threshold the HSV image to obtain input color

    im = cv2.imread(/home/pi/Desktop/DDL/image.jpg)
    width, height = im.shape[:2]

    left = (width - 100)/2
    top = (height -100)/2
    right= (width + 100)/2
    bottom = (height + 100)/2

    im.crop((left, top, right, bottom))
    rgb = im.convert('RGB')
    r, g, b = rgb.pixel((1,1))
    print(r, g, b)

    mask = cv2.inRange(hsv, weaker, stronger)

    cv2.imshow('Image',image)
    cv2.imshow('Result',mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



def LEDs():
    print("Calling: Strobe(strip, 255, 255, 255, 5, .5, 3)")
    Strobe(strip,255,255,255, 5, .6, 3)






#************main*****************

while(1):
	TakePicture() #takes picutre
	print("Complete step 1")
	OpenCVTest() #analyzes picture to see if certain color is in it
	print("Complete step 2")
	LEDs() #strobes LED strip to detected color
	print("Complete step 3")



