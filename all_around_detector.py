# Author: Jeff Yñota
# Date: February 1, 2019

import cv2
import numpy as np
import os

from video_camera import VideoCamera
from record_video import recordVideo

def detect(fgbg, webcam, frameCount,capture,name):
	
    while True:
        mot = ""
        frameCount += 1
        frame = webcam.get_frame()
        fgmask = fgbg.apply(frame)
        count = np.count_nonzero(fgmask)

        if(frameCount > 1 and count > 5000):
            cv2.putText(fgmask, 'Something was Detected', (10, 400),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
            mot = "detected"
        
        if(mot == "detected"):
        	recordVideo(capture, name)

        cv2.imshow("Motion Contour", fgmask)

        if cv2.waitKey(40) & 0xFF == 27:
            cv2.destroyAllWindows()
            break
