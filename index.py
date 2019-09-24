#! env/bin/python3
import cv2
import numpy as np
import matplotlib.pyplot as plt

from modules import skin_detection, convert

_, image = skin_detection.get_skin("./assets/original/skin2.jpg")

cv2.imwrite("./assets/transformed/hsv.png", image)

_, gray_image = convert.gray2color("./assets/original/gray1.jpg")

cv2.imwrite("./assets/transformed/color.png", gray_image)