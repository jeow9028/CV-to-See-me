#This is the function library.  This is imported by main.py

import time
import math
import random
from neopixel import *
from array import *
import argparse
import signal
import sys
import datetime

def signal_handler(signal, frame):
        colorWipe(strip, Color(0,0,0))
        sys.exit(0)

def opt_parse():
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', action='store_true', help='clear the display on exit')
        args = parser.parse_args()
        if args.c:
                signal.signal(signal.SIGINT, signal_handler)

#LED strip configuration:
LED_COUNT      = 15      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

#Define functions which animate LEDs in various ways.
def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

def FadeRGB(strip):
    for i in range(0, 3):
        #Fade In.
        for j in range (0, 256):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()
        #Fade Out.
        for j in range (256, 0, -1):
            if i == 0:
                SetAll(strip, Color(j, 0, 0))
            elif i == 1:
                SetAll(strip, Color(0, j, 0))
            elif i == 2:
                SetAll(strip, Color(0, 0, j))
            strip.show()

def FadeInOut(strip, red, green, blue):
    #Fade In.
    for i in range (0, 256):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()
    #Fade Out.
    for i in range (256, 0, -1):
        r = int(math.floor((i / 256.0) * red))
        g = int(math.floor((i / 256.0) * green))
        b = int(math.floor((i / 256.0) * blue))
        SetAll(strip, Color(r, g, b))
        strip.show()

def Strobe(strip, red, green, blue, StrobeCount, FlashDelay, EndPause):
    for i in range (0, StrobeCount):
        SetAll(strip, Color(red, green, blue))
        strip.show()
        time.sleep(FlashDelay)
        SetAll(strip, Color(0, 0, 0))
        strip.show()
        time.sleep(FlashDelay)
    time.sleep(EndPause)

def Cylon(strip, red, green, blue, EyeSize, SpeedDelay, ReturnDelay):
    for i in range (0, (LED_COUNT - EyeSize - 2)):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
    for i in range ((LED_COUNT - EyeSize - 2), 0, -1):
        SetAll(strip, Color(0, 0, 0))
        strip.setPixelColor(i, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        for j in range(1, (EyeSize + 1)):
            strip.setPixelColor(i + j, Color(red, green, blue))
        strip.setPixelColor(i + EyeSize + 1, Color(int(math.floor(red / 10)), int(math.floor(green / 10)), int(math.floor(blue / 10))))
        strip.show()
        time.sleep(SpeedDelay)
    time.sleep(ReturnDelay)
