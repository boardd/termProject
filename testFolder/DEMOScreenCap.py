import mss
import cv2
import numpy as np
import time

with mss.mss() as sct:
    while True:
        img = np.array(sct.grab(sct.monitors[1]))
        cv2.imshow("image", img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break