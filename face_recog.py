# Author: Jeff Yñota
# Date: February 1, 2019

import cv2
import os
import datetime
      
from IPython.display import clear_output
from video_camera import VideoCamera
from face_function import *

def faceRecog(webcam, detector):
	images, labels, labels_dic = collect_dataset()

	rec_lbph = cv2.face.LBPHFaceRecognizer_create()
	rec_lbph.train(images, labels)

	print("Model Trained Successfully")

	while True:
		frame = webcam.get_frame()
		faces_coord = detector.detect(frame, True)

		cv2.putText(frame, datetime.datetime.now().strftime("%A, %B %d %Y %I:%M:%S %p"), (5, frame.shape[0] - 5),
					cv2.FONT_HERSHEY_PLAIN, 1.3, (66, 53, 243), 2, cv2.LINE_AA)

		if len(faces_coord):
			faces = normalize_faces(frame, faces_coord)
			for i, face in enumerate(faces):
				prediction, confidence = rec_lbph.predict(face)
				threshold = 165
				clear_output(wait=True)
				if(confidence > threshold):
					pred = labels_dic[prediction].capitalize()
					cv2.putText(frame, labels_dic[prediction].capitalize(),
								(faces_coord[i][0], faces_coord[i][1] - 10),
								cv2.FONT_HERSHEY_PLAIN, 3, (66, 53, 243), 2)
				elif(confidence < threshold):
					cv2.putText(frame, "Unknown",
						(faces_coord[i][0], faces_coord[i][1]),
						cv2.FONT_HERSHEY_PLAIN, 3, (66, 53, 243), 2)
				draw_rectangle(frame, faces_coord)
		cv2.imshow("Face Recognition Prototype", frame)

		if cv2.waitKey(40) & 0xFF == 27:
			cv2.destroyAllWindows()
			break
	webcam.video.release()


