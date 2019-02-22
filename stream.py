# Author: Jeff Yñota
# Date: February 15, 2019

import cv2
import os
import datetime
from video_camera import VideoCamera


def stream(webcam):

	cv2.namedWindow("Stream Prototype", cv2.WINDOW_AUTOSIZE) 
	while True:
		frame = webcam.get_frame()

		cv2.putText(frame, datetime.datetime.now().strftime("%A, %B %d %Y %I:%M:%S %p"), (5, frame.shape[0] - 5),
                	cv2.FONT_HERSHEY_PLAIN, 1.3, (66, 53, 243), 2, cv2.LINE_AA)

		cv2.imshow("Stream Prototype", frame)

		if cv2.waitKey(40) & 0xFF == 27:
			cv2.destroyAllWindows()
			break
	webcam.video.release()

