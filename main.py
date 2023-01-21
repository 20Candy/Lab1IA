#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO


import matrixFromImage
import bfs
import paintOnImage

from PIL import Image

def main():

    #menu
    print("Laboratorio 1: Inteligencia Artificial")
    print("1. BFS")
    
    #seleccion de opcion
    opcion = int(input("Ingrese la opcion que desea: "))

    if opcion == 1:

        image = Image.open("prueba1.bmp")
        matrix = matrixFromImage.matrixFromImage(image)
        path = bfs.bfs(matrix)
        paintOnImage.paintOnImage("prueba1.bmp",path)

       