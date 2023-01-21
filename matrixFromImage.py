#from an image get matrix thar represents if a pixels is black or white
# 0 is white and 1 is black

import cv2
import numpy as np

def matrixFromImage(image):

    # read the image
    img = cv2.imread(image)

    # convert the image to the HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define the range of red color in HSV
    lower_red = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
    upper_red = cv2.inRange(hsv, (160, 50, 50), (180, 255, 255))

    # merge the upper and lower range of red
    red_pixels = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

    # define the range of green color in HSV
    lower_green = cv2.inRange(hsv, (40,50,50), (70,255,255))

    # define the range of black color
    lower_black = cv2.inRange(hsv, (0, 0, 0), (180, 255, 30))

    # define the range of white color
    lower_white = cv2.inRange(hsv, (0, 0, 200), (180, 30, 255))

    # create an empty matrix with the same shape as the image
    color_matrix = np.zeros(img.shape[:2], dtype=np.uint8)

    # assign values to the different color pixels
    color_matrix[np.where(red_pixels == 255)] = 2
    color_matrix[np.where(lower_green == 255)] = 3
    color_matrix[np.where(lower_black == 255)] = 0
    color_matrix[np.where(lower_white == 255)] = 1

    return color_matrix
