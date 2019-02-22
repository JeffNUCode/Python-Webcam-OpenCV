# Author: Jeff Yñota
# Date: February 1, 2019

import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
from IPython.display import clear_output

class FaceDetector(object):
    def __init__(self, xml_path):
        self.classifier = cv2.CascadeClassifier(xml_path)

    def detect(self, image, biggest_only):
        scale_factor = 1.2
        min_neighbours = 5
        min_size = (30, 30)
        biggest_only = True
        flags = cv2.CASCADE_FIND_BIGGEST_OBJECT | \
            cv2.CASCADE_DO_ROUGH_SEARCH if biggest_only else \
            cv2.CASCADE_SCALE_IMAGE

        faces_coord = self.classifier.detectMultiScale(image,
                                                       scaleFactor=scale_factor,
                                                       minNeighbors=min_neighbours,
                                                       minSize=min_size,
                                                       flags=flags)
        return faces_coord