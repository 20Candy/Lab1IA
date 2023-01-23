from collections import deque
import nodos

class astar():

    def __init__(self, matrix, heuristic):
        self.matrix = matrix
        self.heuristic = heuristic

        self.endings = self.possible_endings()

        start = self.find_start()
        path = self.astar(start)

        self.path = path
    

    def find_start(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 2:
                    return (i, j)
        return None

    def possible_endings(self):
        endings = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 3:
                    endings.append((i, j))
        return endings

    def actions(self, state):
        x, y = state
        actions = []
        if x > 0 and self.matrix[x-1][y] != 0:
            actions.append("up")
        if x < len(self.matrix)-1 and self.matrix[x+1][y] != 0:
            actions.append("down")
        if y > 0 and self.matrix[x][y-1] != 0:
            actions.append("left")
        if y < len(self.matrix[0])-1 and self.matrix[x][y+1] != 0:
            actions.append("right")
        return actions

    def result(self, state, action):
        x, y = state
        if action == "up":
            return (x-1, y)
        elif action == "down":
            return (x+1, y)
        elif action == "left":
            return (x, y-1)
        elif action == "right":
            return (x, y+1)

    def goalTest(self, state):
        x, y = state
        return (self.matrix[x][y] == 3)

    def stepCost(self, state, action):
        return 1 # all steps have the same cost

    def pathCost(self, begin, end):
        if(self.heuristic == 'Manhattan'):
            return self.pathCostManhattan(begin, end)
        elif(self.heuristic == 'Euclidean'):
            return self.pathCostEuclidean(begin, end)

    def pathCostManhattan(self, begin, end):
        x1, y1 = begin
        x2, y2 = end
        return abs(x2-x1) + abs(y2-y1)
    
    def pathCostEuclidean(self, begin, end):
        x1, y1 = begin
        x2, y2 = end
        return ((x2-x1)**2 + (y2-y1)**2)**0.5

    def astar(self, start):

        shortestPath = []

        nodeMatrix = []
        for i in range(len(self.matrix)):
            nodeMatrix.append([])
            for j in range(len(self.matrix[i])):

                tempNode = nodos.nodos((i, j))
                nodeMatrix[i].append(tempNode)
        
        for end in self.endings:
            visited = []
            visited.append(start)
  
            start_Node = nodeMatrix[start[0]][start[1]]

            start_Node.setG(0)
            start_Node.setH(self.pathCost(start, end))
            start_Node.setF()
            start_Node.setVisited()

            while True:
                nodes_checked = 0
                nodo = visited[-1]
                actions = self.actions(nodo)

                for action in actions:

                    next = self.result(nodo, action)

                    if next not in visited:
                        nodoObj = nodeMatrix[nodo[0]][nodo[1]]
                        nextObj = nodeMatrix[next[0]][next[1]]

                        nextObj.parent = nodoObj
                        nextObj.setG(nodoObj.g + self.stepCost(nodo, action))
                        nextObj.setH(self.pathCost(next, end))
                        nextObj.setF()

                    if next in visited:
                        nodoObj = nodeMatrix[nodo[0]][nodo[1]]
                        nextObj = nodeMatrix[next[0]][next[1]]

                        if nextObj.f >= nextObj.h + nextObj.g + self.stepCost(nodo, action):
                            nextObj.parent = nodoObj
                            nextObj.setG(nodoObj.g + self.stepCost(nodo, action))
                            nextObj.setF()
                            nextObj.visited = False

                find = False
                for nodes in nodeMatrix:
                    #look for the node with the lowest f value that has not been visited yet
                    # if tie, pick lowest h value
                    nodes.sort(key=lambda x: x.f)


                    for node in nodes:
                        if node.visited == False:
                            node.visited = True
                            visited.append(node.position)
                            find = True
                            break
                    if find:
                        break

                if self.goalTest(visited[-1]):
                    shortestPath = visited
                    break

                if nodes_checked == len(visited):
                    shortestPath = []
                    break

                nodes_checked += 1

            return shortestPath