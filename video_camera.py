# Author: Jeff Yñota
# Date: February 1, 2019

import cv2
import os

class VideoCamera(object):
    def __init__(self, index=0):
        self.video = cv2.VideoCapture(0)
        self.index = index
        print(self.video.isOpened())

    def __del__(self):
        self.video.release()

    def get_frame(self, in_grayscale=False):
        _, frame = self.video.read()
        if in_grayscale:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return frame
