from queue import PriorityQueue
import numpy as np

def aStar(startNode, goalNode, nodes, graph, coordinates):
    goalNodeIdx = nodes.index(goalNode)

    # Inisiialisasi dictionary jarak dan priority queue
    distances = {node: float('inf') for node in nodes}
    distances[startNode] = 0

    pq = PriorityQueue()
    pq.put((distances[startNode], startNode))

    # Inisialisasi dictionary parent dan total cost
    parents = {startNode: None}

    while not pq.empty():
        currNode = pq.get()[1]

        if currNode == goalNode:
            # Goal node ditemukan
            path = []
            while currNode is not None:
                path.append(currNode)
                currNode = parents[currNode]
            path.reverse()
            return path, evaluate

        for neighborIdx in range(len(nodes)):
            # Cek apakah node terhubung
            if graph[nodes.index(currNode)][neighborIdx] > 0:
                neighbor = nodes[neighborIdx]
                # Menghitung jarak dari current node ke neighbor node
                gN = distances[currNode] + graph[nodes.index(currNode)][neighborIdx]
                # Cek apakah jarak dari current node ke neighbor node lebih kecil dari jarak sebelumnya
                if gN < distances[neighbor]:
                    # Mengupdate jarak dan parent node
                    distances[neighbor] = gN
                    parents[neighbor] = currNode
                    # Menghitung heuristic distance
                    heuristicDist = straightline(coordinates[neighborIdx], coordinates[goalNodeIdx])
                    # Menghitung evaluation function ( f(n) = g(n) + h(n) )
                    evaluate = gN + heuristicDist
                    # Menambahkan neighbor node ke priority queue
                    pq.put((evaluate, neighbor))

    # Jika path menuju goal node dan cost tidak ditemukan maka akan mengembalikan None
    return None, None

def straightline(coordinate1, coordinate2):
    # Menghitung jarak antara dua titik
    return np.linalg.norm(np.array(coordinate1) - np.array(coordinate2))
