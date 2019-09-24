import cv2
import numpy as np
import matplotlib.pyplot as plt

def gray2color(image):
  image_BGR = cv2.imread(image)
  colored_image = cv2.applyColorMap(image_BGR, cv2.COLORMAP_INFERNO)

  return colored_image, np.hstack([image_BGR, colored_image])