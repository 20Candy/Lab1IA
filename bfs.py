#from a given matrix with 0 and 1, find the shortest path from 2 to 3
# 0 is white and 1 is black
# 2 is red and 3 is green
# 2 is the start and 3 is the end

def bfs(matrix):
    #find the start
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                start = (i,j)
                break
    #find the end
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 3:
                end = (i,j)
                break
    #create a queue
    queue = []  
    queue.append(start)
    #create a visited list
    visited = []
    #create a parent list
    parent = []
    #create a path list
    path = []
    #create a distance list
    distance = []
    #create a distance from start to start
    distance[start] = 0

    while queue:
        #pop the first element in the queue
        current = queue.pop(0)
        #if current is the end, break
        if current == end:
            break
        #if current is not visited, mark it as visited
        if current not in visited:
            visited.append(current)
        #get the neighbors of current
        neighbors = getNeighbors(current)
        #for each neighbor
        for neighbor in neighbors:
            #if neighbor is not visited
            if neighbor not in visited:
                #add neighbor to queue
                queue.append(neighbor)
                #add neighbor to parent list
                parent[neighbor] = current
                #add neighbor to distance list
                distance[neighbor] = distance[current] + 1

    #create the path
    current = end
    while current != start:
        path.append(current)
        current = parent[current]

    path.append(start)
    return path

def getNeighbors(current):
    neighbors = []
    #get the neighbors of current
    #if current is not in the first row
    if current[0] != 0:
        #add the neighbor above
        neighbors.append((current[0]-1,current[1]))
    #if current is not in the last row
    if current[0] != len(matrix)-1:
        #add the neighbor below
        neighbors.append((current[0]+1,current[1]))
    #if current is not in the first column
    if current[1] != 0:
        #add the neighbor to the left
        neighbors.append((current[0],current[1]-1))
    #if current is not in the last column
    if current[1] != len(matrix[0])-1:
        #add the neighbor to the right
        neighbors.append((current[0],current[1]+1))

    return neighbors
