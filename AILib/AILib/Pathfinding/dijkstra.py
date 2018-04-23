"""
Matthew Sabo
Dijkstra
Copywrite 2018
"""

from bfs import SquareGrid
from Queue import PriorityQueue
import time

class WeightedGrid(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                if ((x, y) in self.path): print("* ", end='')
                elif ((x, y) in self.walls): print("X ", end ='')
                else: print("%d " % self.weights[(x, y)], end='')
            print("\n")

def dijkstra(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    visited = {}
    cost_so_far = {}
    visited[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal: break
        for next in grid.neighbors(current):
            new_cost = cost_so_far[current] + grid.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                visited[next] = current

    return visited, cost_so_far

def build_path(visited, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = visited[current]
    path.append(start)
    path.reverse()
    return path

grid = WeightedGrid(15, 15)
grid.walls = [(7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9)]
for x in range(15):
    for y in range(15):
        grid.weights[(x, y)] = 1

for x in range(6):
    for y in range(4):
        grid.weights[(x+1, y+10)] = 9

grid.print()
print("\n\n")

start = time.time()
(visited, costs) = dijkstra(grid, (1, 4), (14, 11))
end = time.time()
print("Dijkstra time: %f" %(end-start))
path = build_path(visited, (1, 4), (14, 11))
grid.path = path
grid.print()