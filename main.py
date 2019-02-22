# Author: Jeff Yñota
# Date: February 17, 2019

import cv2
import os
import time
import threading
from video_camera import VideoCamera
from face_detector import FaceDetector

from stream import stream
from all_around_detector import detect
from fire_detection import fire_detect
from face_recog import faceRecog

webcam = VideoCamera()

fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)
frameCount = 0
name_detect = "DETECTED"
name_fire = "FIRE"

detector = FaceDetector(
    "C:/Users/JeffRolan11/jeff_python/xml/frontal_face.xml")



if __name__ == "__main__":  
	#c1 = threading.Thread(name = 'c1', target = stream, args = (webcam,))
	#c2 = threading.Thread(name = 'c2', target = fire_detect, args = (webcam,webcam,name_fire,))
	#c3 = threading.Thread(name = 'c3', target = detect, args = (fgbg,webcam,frameCount,webcam,name_detect,))
	c4 = threading.Thread(name = 'c4', target = faceRecog, args = (webcam,detector,))

	#c1.start()
	#time.sleep(2)
	#c2.start()
	#time.sleep(2)
	#c3.start()
	#time.sleep(2)
	c4.start()


