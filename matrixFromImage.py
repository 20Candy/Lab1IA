#from an image get matrix thar represents if a pixels is black or white
# 0 is white and 1 is black

import cv2
import sys

def matrixFromImage(image):

    img = cv2.imread(image)

    height, width, _ = img.shape

    matrix = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            b, g, r = img[y, x]
            if (b, g, r) == (0, 0, 0): # black
                matrix[y][x] = 0
            elif (b, g, r) == (255, 255, 255): # white
                matrix[y][x] = 1
            elif (b, g, r) == (0, 0, 255): # red
                matrix[y][x] = 2
            elif (b, g, r) == (0, 255, 0): # green
                matrix[y][x] = 3
    return matrix
