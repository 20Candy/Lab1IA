from collections import deque

def bfs(matrix):

    #serach for start and edn
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                end = (x, y)

    queue = deque([start])

    visited = []

    shortest_path = []

    while queue:
        x, y = queue.popleft()

        visited.append((x, y))

        # Check if we have reached the end
        if matrix[y][x] == 3:
            while (x, y) != start:
                shortest_path.append((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (x+dx, y+dy) in visited:
                        x, y = x+dx, y+dy
                        break
            shortest_path.reverse()
            return shortest_path
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < len(matrix[0]) and 0 <= y+dy < len(matrix) and matrix[y+dy][x+dx] != 1 and (x+dx, y+dy) not in visited:
                queue.append((x+dx, y+dy))
    return None
