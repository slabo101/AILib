"""
Matthew Sabo
astar
Copywrite 2018
"""

from dijkstra import WeightedGrid
from dijkstra import build_path
from Queue import PriorityQueue
import time

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1-x2)+ abs(y1-y2)

def a_star(grid, start, goal):
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
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                visited[next] = current

    return visited, cost_so_far

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
(visited, costs) = a_star(grid, (1, 4), (14, 11))
end = time.time()
print("A* time: %f" %(end-start))
path = build_path(visited, (1, 4), (14, 11))
grid.path = path
grid.print()