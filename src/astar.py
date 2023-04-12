import heapq
import numpy as np

def aStar(graph, startString, goalString, nodes, coordinates):
    start = nodes.index(startString)
    goal = nodes.index(goalString)
    costQueue = [(0, start, [])]
    prioQueue = [(straightLine(coordinates[start], coordinates[goal]), start)]
    visited = set()
    while costQueue:
        (cost, currNode, path) = heapq.heappop(costQueue)
        if currNode == goal:
            return path + [currNode], cost
        if currNode not in visited:
            visited.add(currNode)
            for neighbor in range(len(graph[currNode])):
                if graph[currNode][neighbor] != 0:
                    newCost = cost + graph[currNode][neighbor]
                    newPath = path + [currNode]
                    heapq.heappush(costQueue, (newCost, neighbor, newPath))
                    heuristicCost = straightLine(coordinates[neighbor], coordinates[goal])
                    heapq.heappush(prioQueue, (newCost + heuristicCost, neighbor))
    return None, None

def straightLine(coordinate1, coordinate2):
    return np.linalg.norm(np.array(coordinate1) - np.array(coordinate2))
