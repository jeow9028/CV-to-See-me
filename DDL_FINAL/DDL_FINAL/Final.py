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
    #weaker = np.array([65,60,60])
    #stronger = np.array([80,255,255])

    #BLUE
    #weaker = np.array([90,50,50])
    #stronger = np.array([150,255,255])

    #RED
    weaker = np.array([0,50,50])
    stronger = np.array([10,255,255])

    #Threshold the HSV image to obtain input color


    mask = cv2.inRange(hsv, weaker, stronger)

    cv2.imshow('Image',image)
    cv2.imshow('Result',mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    im = Image.open('/home/pi/Desktop/DDL/Image.jpg')
    width, height = im.size

    left = (width -0)/2
    top = (height -0)/2
    right= (width + 0)/2
    bottom = (height + 0)/2

    im.crop((left, top, right, bottom))
    rgb = im.convert('RGB')
    r, g, b = rgb.getpixel((1,1))


    print("RGB Values:	",r, g, b)
    print("Weaker/Stronger:	",weaker, stronger)

    print("/n")
    print("Light Test colour")

#RED
    if ((150<r<250) and (0<g<250) and (0<b<250)):
        print("Calling: RED")
        Strobe(strip,250,250,250, 5, .6, 3)
#GREEN
    elif ((0<r<250) and (150<g<250) and (0<b<250)):
        print("Calling: Green")
        Strobe(strip,0,255,255, 5, .6, 3)
#BLUE
    elif ((0<r<250) and (0<g<250) and (150<b<250)):
        print("Calling: BLUE")
        Strobe(strip,0,0,250, 5, .6, 3)

#************main*****************

while(1):
    TakePicture() #takes picutre
    print("Complete step 1")
    OpenCVTest() #analyzes picture to see if certain color is in it
    print("Complete step 2")
    print("Misssion Complete")

   # LEDs() #strobes LED strip to detected color
   # print("Complete step 3")




