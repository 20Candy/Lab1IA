def dfs(matrix):

    matrix = [[1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 2, 0, 1],
    [1, 1, 1, 3, 1]]

    start = None
    goal = None

    #serach for start and end
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 2:
                start = (i, j)
            elif matrix[i][j] == 3:
                goal = (i, j)


    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next_vertex in get_adjacent_vertices(matrix, vertex):
            if next_vertex in path:
                continue
            if next_vertex == goal:
                return path + [next_vertex]
            stack.append((next_vertex, path + [next_vertex]))
    return None

def get_adjacent_vertices(matrix, vertex):
    x, y = vertex
    rows = len(matrix)
    cols = len(matrix[0])
    adjacent_vertices = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    adjacent_vertices = [(x, y) for x, y in adjacent_vertices if 0 <= x < rows and 0 <= y < cols and matrix[x][y] != 1]
    return adjacent_vertices

