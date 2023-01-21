#from an image get matrix thar represents if a pixels is black or white
# 0 is white and 1 is black

from PIL import Image
import sys

def matrixFromImage(image):

    new_image = image.resize((50,50))
    new_image.save("prueba1_short.bmp")

    height, width, _ = new_image.shape

    matrix = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            b, g, r = new_image[y, x]
            if (b, g, r) == (0, 0, 0): # black
                matrix[y][x] = 0
            elif (b, g, r) == (255, 255, 255): # white
                matrix[y][x] = 1
            elif (b, g, r) == (0, 0, 255): # red
                matrix[y][x] = 2
            elif (b, g, r) == (0, 255, 0): # green
                matrix[y][x] = 3
    return matrix
