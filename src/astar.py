import heapq
import numpy as np

def aStar(start, goal, nodes, graph, coordinates):
    start = nodes.index(start)
    goal = nodes.index(goal)
    cost_queue = [(0, start, [])]  # jarak, simpul, lintasan
    priority_queue = [(straightline(coordinates[start], coordinates[goal]), start)]
    visited = set()
    while cost_queue:
        (cost, current_node, path) = heapq.heappop(cost_queue)
        if current_node == goal:
            return path + [current_node], cost
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in range(len(graph[current_node])):
                if graph[current_node][neighbor] != 0:
                    new_cost = cost + graph[current_node][neighbor]
                    new_path = path + [current_node]
                    heapq.heappush(cost_queue, (new_cost, neighbor, new_path))
                    heuristic_cost = straightline(coordinates[neighbor], coordinates[goal])
                    heapq.heappush(priority_queue, (new_cost + heuristic_cost, neighbor))

    return [], None

def straightline(coordinate1, coordinate2):
    # Menghitung jarak antara dua titik
    return np.linalg.norm(np.array(coordinate1) - np.array(coordinate2))
