import cv2
import numpy as np

def solidBackground(shape = (480, 640, 3), color = (0, 255, 0)):
    bg_image = np.ones(shape, dtype = np.uint8)
    bg_image[:] = color
    return bg_image

def imageBackground(source):
    return cv2.imread(source)