#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO

import matrixFromImage
import bfs
import dfs
import astar
import paintOnImage
import toPixelArt

def main():
    print("\nArchivos disponibles:")
    print("1. Prueba 1")
    print("2. Prueba 2")
    print("3. Prueba 3")

    opcion = int(input("Ingrese la opcion que desea: "))

    if opcion == 1:
        file = "prueba1.bmp"
    elif opcion == 2:
        file = "prueba2.bmp"
    elif opcion == 3:
        file = "prueba3.bmp"


    #menuwith while
    while True:
        print("\nInteligencia Artificial")

        print("\n1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. Salir")
        
        #seleccion de opcion
        opcion = int(input("Ingrese la opcion que desea: "))

        toPixelArt.toPixelArt(file)
        matrix = matrixFromImage.matrixFromImage("pixelart.bmp")

        if opcion == 1:
            path = bfs.bfs(matrix)
            print(path)


        elif opcion == 2:
            path = dfs.dfs(matrix)
            print(path)


        elif opcion == 3:
            #astar
            heristica = input("\nA* / Ingrese la heuristica que desea: \n 1. Manhattan \n 2. Euclidea\n")
            if(heristica == '1'):
                astarPath = astar.astar(matrix, 'Manhattan')
                path = astarPath.path
                
            elif(heristica == '2'):
                astarPath = astar.astar(matrix, 'Euclidean')
                path = astarPath.path
            
            print(path)


        elif opcion == 4:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")

        paintOnImage.paintOnImage("pixelart.bmp",path)


if __name__ == "__main__":
    main()


       