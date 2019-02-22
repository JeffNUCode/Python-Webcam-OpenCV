# Author: Jeff Yñota
# Date: February 1, 2019

import cv2
import numpy as np
import os
from video_camera import VideoCamera


def cut_faces(image, faces_coord):
    faces = []
    for (x, y, w, h) in faces_coord:
        w_rm = int(0.2 * w / 2)  # only 70, 80% of the wdithh
        faces.append(image[y: y + h, x + w_rm: x + w - w_rm])

    return faces


def normalize_intensity(images):
    images_norm = []
    for image in images:
        is_color = len(image.shape) == 3
        if is_color:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images_norm.append(cv2.equalizeHist(image))
    return images_norm


def resize(images, size=(50, 50)):
    images_norm = []
    for image in images:
        if image.shape < size:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        else:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)

        images_norm.append(image_norm)

    return images_norm


def normalize_faces(frame, faces_coord):
    faces = cut_faces(frame, faces_coord)
    faces = normalize_intensity(faces)
    faces = resize(faces)
    return faces


def draw_rectangle(image, coords):
    for(x, y, w, h) in coords:
        w_rm = int(0.2 * w / 2)
        cv2.rectangle(image, (x + w_rm, y),
                      (x + w - w_rm, y + h), (150, 150, 0), 8)


def collect_dataset():
    images = []
    labels = []
    labels_dic = {}
    file_path = "C:/Users/JeffRolan11/jeff_python/people/"
    people = [person for person in os.listdir(file_path)]
    for i, person in enumerate(people):
        labels_dic[i] = person
        for image in os.listdir(file_path + person):
            images.append(cv2.imread(
                file_path + person + '/' + image, 0))
            labels.append(i)
    return (images, np.array(labels), labels_dic)




