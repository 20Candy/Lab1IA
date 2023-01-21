def dfs(matrix):

    # matrix = [[1, 1, 1, 1, 1],
    #     [1, 0, 0, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 0, 2, 0, 1],
    #     [1, 1, 1, 3, 1]]

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                end = (x, y)

    stack = [(start, [start])]
    visited = set()

    while stack:
        (vertex, path) = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            x, y = vertex
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                if 0<=x+dx<len(matrix) and 0<=y+dy<len(matrix[0]) and matrix[x+dx][y+dy]!=1:
                    if (x+dx, y+dy) == end:
                        
                        return path + [(x+dx, y+dy)]
                    else:
                        stack.append(((x+dx, y+dy), path + [(x+dx, y+dy)]))

    return None
