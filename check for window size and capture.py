import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision


while True:
    wincap =  WindowCapture('BlueStacks')
    print(wincap.get_screen_position())
    wincap.take_SS('testimage.jpg')
    time.sleep(0.05)
