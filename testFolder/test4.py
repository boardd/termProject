# name/text detection

from cmu_112_graphics import *
from PIL import ImageTk
from PIL import Image
import numpy as np
import imutils
from imutils.video import FileVideoStream
from imutils.video import FPS
import cv2
import mss
import time
import pytesseract

# constants 
blue = (255,0,0) # BGR not RGB
green = (0, 255, 0)
red = (0,0,255)

scale = 3
upperLimit = int(210/scale)
lowerLimit = int(60/scale)

# tess data is stored at "/usr/local/share/tessdata"

pytesseract.pytesseract.tesseract_cmd = r"/Users/tony/tesseract/build/tesseract"
img = cv2.imread("resources/sampleText.png")
rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(rgbImg))

cv2.imshow("result",rgbImg)
cv2.waitKey(0)
