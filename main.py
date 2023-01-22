#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO


import matrixFromImage
import bfs
import dfs
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

        # toPixelArt.toPixelArt("prueba1.bmp")
        # matrix = matrixFromImage.matrixFromImage("pixelart.bmp")

        # print(matrix)

        if opcion == 1:
            path = bfs.bfs()
            print(path)


        elif opcion == 2:
            path = dfs.dfs()
            print(path)


        elif opcion == 3:
            print("Opcion 3")
        elif opcion == 4:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")

        # paintOnImage.paintOnImage("prueba1.bmp",path)


if __name__ == "__main__":
    main()


       