#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO


import matrixFromImage
import bfs
import paintOnImage
import toPixelArt

from PIL import Image

def main():

    #menuwith while

    while True:
        print("\nInteligencia Artificial")

        print("\n1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. Salir")
        
        #seleccion de opcion
        opcion = int(input("Ingrese la opcion que desea: "))

        if opcion == 1:

            toPixelArt.toPixelArt("prueba1.bmp")
            matrix = matrixFromImage.matrixFromImage("pixelart.bmp")
            path = bfs.bfs(matrix)
            paintOnImage.paintOnImage("prueba1.bmp",path)

        if opcion == 2:
            print("Opcion 2")
        if opcion == 3:
            print("Opcion 3")
        if opcion == 4:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")


if __name__ == "__main__":
    main()


       