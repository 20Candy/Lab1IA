from collections import deque

def bfs(matrix):

    def find_start():
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 2:
                    return (i, j)
        return None

    def actions(state):
        x, y = state
        actions = []
        if x > 0 and matrix[x-1][y] != 0:
            actions.append("up")
        if x < len(matrix)-1 and matrix[x+1][y] != 0:
            actions.append("down")
        if y > 0 and matrix[x][y-1] != 0:
            actions.append("left")
        if y < len(matrix[0])-1 and matrix[x][y+1] != 0:
            actions.append("right")
        return actions

    def result(state, action):
        x, y = state
        if action == "up":
            return (x-1, y)
        elif action == "down":
            return (x+1, y)
        elif action == "left":
            return (x, y-1)
        elif action == "right":
            return (x, y+1)

    def goalTest(state):
        x, y = state
        return matrix[x][y] == 3

    def stepCost(state, action):
        return 1 # all steps have the same cost

    def pathCost(path):
        return len(path) - 1

    def BFS(start):
        queue = deque([(start, [start])])
        visited = set()
        while queue:
            state, path = queue.popleft()
            if goalTest(state):
                return path
            if state in visited:
                continue
            visited.add(state)
            for action in actions(state):
                new_state = result(state, action)
                new_path = path + [new_state]
                queue.append((new_state, new_path))
        return None

    start = find_start()
    path = BFS(start)
    if path:
        return path
    
    return None
