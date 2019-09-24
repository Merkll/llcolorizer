import cv2
import numpy as np
import matplotlib.pyplot as plt

min_HSV = np.array([0, 58, 30], dtype = "uint8")
max_HSV = np.array([33, 255, 255], dtype = "uint8")

def get_skin_region(image):
  image_BGR = cv2.imread(image)
  image_HSV = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2HSV)

  return cv2.inRange(image_HSV, min_HSV, max_HSV), image_BGR


def get_skin(image):
  skin_region, image_BGR = get_skin_region(image)
  image_HSV = cv2.bitwise_and(image_BGR, image_BGR, mask = skin_region)

  return image_HSV, np.hstack([image_BGR, image_HSV])