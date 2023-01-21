#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO


import matrixFromImage
import bfs

from PIL import Image

def main():
    image = Image.open("prueba1.bmp")
    matrix = matrixFromImage.matrixFromImage(image)
    path = bfs.bfs(matrix)
    print(path)