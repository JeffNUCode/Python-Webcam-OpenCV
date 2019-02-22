# Author: Jeff Yñota
# Date: February 12, 2019

import cv2
import numpy as np
import os
from video_camera import VideoCamera
from record_video import recordVideo

def fire_detect(webcam, capture, name):
	while True:
		detect = ""
		frame = webcam.get_frame()
		blur = cv2.GaussianBlur(frame, (21, 21), 0)
		hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
		lower = [18, 50, 50]
		upper = [35, 255, 255]
		lower = np.array(lower, dtype="uint8")
		upper = np.array(upper, dtype="uint8")
		mask = cv2.inRange(hsv, lower, upper)
		output = cv2.bitwise_and(frame, hsv, mask=mask)
		no_red = cv2.countNonZero(mask)

		if int(no_red) > 2000:
			detect = "fire"
			cv2.putText(output, 'Fire Detected', (10, 400),
						cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
			print("FIRE")

		if(detect == "fire"):
			recordVideo(capture, name)

		cv2.imshow("Fire Detection", output)

		if cv2.waitKey(40) & 0xFF == 27:
			cv2.destroyAllWindows()
			break

