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

vidDir = "video1.mov"

fvs  = FileVideoStream(vidDir).start()
time.sleep(1.0)

fps = FPS().start()

while fvs.more():
	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale (while still retaining 3
	# channels)
	frame = fvs.read()
	frame = imutils.resize(frame, width=720)
	# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# frame = np.dstack([frame, frame, frame])
	# display the size of the queue on the frame
	cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
		(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
	# show the frame and update the FPS counter
	cv2.imshow("Frame", frame)
	cv2.waitKey(1)
	fps.update()

fps.stop()
print(fps.elapsed())
print(fps.fps())
fvs.stop()