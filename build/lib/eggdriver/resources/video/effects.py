import cv2
import numpy as np
import mediapipe as mp

def removeBG(image):
    mp_selfie_segmentation = mp.solutions.selfie_segmentation
    selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection = 1)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = selfie_segmentation.process(image)
    _, th = cv2.threshold(results.segmentation_mask, 0.75, 255, cv2.THRESH_BINARY)
    th = th.astype(np.uint8)
    th_inv = cv2.bitwise_not(th)
    return th, th_inv

def maskImage(image, mask):
    return cv2.bitwise_and(image, image, mask = mask)

def blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)
