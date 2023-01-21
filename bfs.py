from collections import deque

def bfs(matrix):

    matrix = [[1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 2, 0, 1],
        [1, 1, 1, 3, 1]]

    #initializing start and end
    start = None
    end = None

    #serach for start and end
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

            print(shortest_path)
            return shortest_path
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x+dx < len(matrix[0]) and 0 <= y+dy < len(matrix) and matrix[y+dy][x+dx] != 1 and (x+dx, y+dy) not in visited:
                queue.append((x+dx, y+dy))

    print("No path found")
    return None
