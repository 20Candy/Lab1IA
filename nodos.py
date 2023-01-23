#node to represent each point in a matrix for a* algorithm

class nodos:

    def __init__(self, position=None, visited=False, parent=None):
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        self.visited = visited
        self.parent = parent

    def setG(self, g):
        self.g = g

    def setH(self, h):
        self.h = h
    
    def setF(self):
        self.f = self.g + self.h

    def setVisited(self):
        self.visited = True


