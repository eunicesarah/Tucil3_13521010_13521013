import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [])]  # jarak, simpul, lintasan
    visited = set()
    while queue:
        (cost, current_node, path) = heapq.heappop(queue)
        if current_node == goal:
            return path + [current_node], cost  # tambahkan biaya total ke hasil
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in range(len(graph[current_node])):
                if graph[current_node][neighbor] != 0:
                    new_cost = cost + graph[current_node][neighbor]
                    heapq.heappush(queue, (new_cost, neighbor, path + [current_node]))
 
    return [], 0