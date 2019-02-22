# Author: Jeff Yñota
# Date: February 15, 2019

import cv2
import os
import datetime
import time
from video_camera import VideoCamera

def recordVideo(capture, name):
	date = datetime.datetime.now().strftime("%m-%d-%Y,%I-%M-%S-%p")
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(name +" "+date + '.avi', fourcc, 20.0, (640, 480))
	duration = 10
	start = time.time()

	while(int(time.time() - start) < duration):
		frames = capture.get_frame()
		cv2.putText(frames, datetime.datetime.now().strftime("%A, %B %d %Y %I:%M:%S %p"), (5, frames.shape[0] - 5),
					cv2.FONT_HERSHEY_PLAIN, 1.3, (66, 53, 243), 2, cv2.LINE_AA)

		if(int(time.time() - start) < duration):
			out.write(frames)
		else:
			out.release()
			break
