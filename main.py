#INELIGENCIA ARTIFICIAL
#AUTORES: STEFANO ARAGONI, LUIS DIEGO SANTOS, CAROL AREVALO

import modules.matrixFromImage as matrixFromImage
import modules.bfs as bfs
import modules.dfs as dfs
import modules.astar as astar
import modules.paintOnImage as paintOnImage
import modules.toPixelArt as toPixelArt

def main():
    print("\nArchivos disponibles:")
    print("1. Prueba 1")
    print("2. Prueba 2")
    print("3. Prueba 3")

    opcion = int(input("Ingrese la opcion que desea: "))

    if opcion == 1:
        file = "tests/prueba1.bmp"
    elif opcion == 2:
        file = "tests/prueba2.bmp"
    elif opcion == 3:
        file = "tests/prueba3.bmp"


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
        matrix = matrixFromImage.matrixFromImage("temp/pixelart.bmp")

        if opcion == 1:
            path = bfs.bfs(matrix)

        elif opcion == 2:
            path = dfs.dfs(matrix)

        elif opcion == 3:
            #astar
            heristica = input("\nA* / Ingrese la heuristica que desea: \n 1. Manhattan \n 2. Euclidea\n")
            if(heristica == '1'):
                astarPath = astar.astar(matrix, 'Manhattan')
                path = astarPath.path
                
            elif(heristica == '2'):
                astarPath = astar.astar(matrix, 'Euclidean')
                path = astarPath.path

        elif opcion == 4:
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion no valida")

        paintOnImage.paintOnImage("temp/pixelart.bmp",path)


if __name__ == "__main__":
    main()


       