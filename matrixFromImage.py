#from an image get matrix thar represents if a pixels is black or white
# 0 is white and 1 is black

from PIL import Image
import sys

def matrixFromImage(image):

    new_image = image.resize((50,50))
    new_image.save("prueba1_short.bmp")

    #image = Image.open(image)
    width, height = new_image.size
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            if image.getpixel((x,y)) == (0,0,0):
                row.append(1)
            elif image.getpixel((x,y)) == (255,0,0):
                row.append(2)#red
            elif image.getpixel((x,y)) == (0,255,0):
                row.append(3)#green
            elif image.getpixel((x,y)) == (255,255,255):
                row.append(0)

        matrix.append(row)
    return matrix
