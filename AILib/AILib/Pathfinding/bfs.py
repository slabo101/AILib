"""
Matthew Sabo
Breadth First Search
Copywrite 2018
"""

from Queue import Queue

class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.path = []

    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        results = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        if (x+y)%2 == 0: results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if ((x, y) in self.path): print("*", end='')
                elif ((x, y) in self.walls): print("X", end ='')
                else: print(".", end='')
            print("\n")


def simple_bfs(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        if current == goal: break
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def grid_bfs(grid, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = None

    while not frontier.empty():
        current = frontier.get()
        if current == goal: break
        for next in grid.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = current
    return visited

def build_path(visited, goal, start):
    current = goal
    path = []
    while current != start:
        print(current)
        path.append(current)
        current = visited[current]
    path.append(start)
    path.reverse()
    return path

example_graph = SimpleGraph()
example_graph.edges = {
    'A':['B'],
    'B':['A', 'C', 'D'],
    'C':['A'],
    'D':['E', 'A'],
    'E':['B'],
    }

simple_bfs(example_graph, 'A', 'E')

grid = SquareGrid(30, 15)
grid.walls = [(15, 5), (15, 6), (15, 7), (15, 8), (15, 9), (15, 10), (15, 11), (15, 12), (15, 13),
              (20, 0), (20, 1), (20, 2), (20, 3), (20, 4), (21, 4), (22, 4)]
visited = grid_bfs(grid, (1, 8), (21, 2))
path = build_path(visited, (21, 2), (1, 8))
grid.path = path
grid.print()