import heapq

def ucs(graph, startString, goalString, nodes):
    start = nodes.index(startString)
    goal = nodes.index(goalString)
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, currNode, path) = heapq.heappop(queue)
        if currNode == goal:
            return path + [currNode], cost
        if currNode not in visited:
            visited.add(currNode)
            for neighbor in range(len(graph[currNode])):
                if graph[currNode][neighbor] != 0:
                    newCost = cost + graph[currNode][neighbor]
                    heapq.heappush(queue, (newCost, neighbor, path + [currNode]))
    return None, None