
from PIL import Image
import numpy as np

def matrixFromImage(image):

    image = Image.open(image)
    pixels = image.load()

    width, height = image.size
    color_matrix = [[0 for _ in range(width)] for _ in range(height)]

    red_like = 200
    green_like= 200

    # Iterate through the pixels
    for i in range(width):
        for j in range(height):
            # Get the pixel color
            r, g, b = pixels[i, j]

            # Compare the color to the given values
            if r == 0 and g == 0 and b == 0:
                color_matrix[i][j] = 0  # Black
            elif r == 255 and g == 255 and b == 255:
                color_matrix[i][j] = 1  # White
            elif r > red_like and g < red_like and b < red_like:
                color_matrix[i][j] = 2  # Red-like
            elif r < green_like and g > green_like and b < green_like:
                color_matrix[i][j] = 3  # Green-like


    return color_matrix
