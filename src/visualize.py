import networkx as nx
import matplotlib.pyplot as plt
import gmplot
import webbrowser
import os

def printPath(path, cost):
    if path is None and cost is None:
        print("Tidak ditemukan path menuju goal node!")
    else:
        print("Path: ", end='')
        for i in range(len(path)):
            if i == len(path) - 1:
                print(path[i])
            else:
                print(path[i], end=' -> ')
        print("Cost: ", cost)

def showGraph(nodes, graph, path, coordinates):
    print("Showing graph...")
    showMap(nodes, graph, path, coordinates)
    webbrowser.open(os.getcwd() + "\\bin\\map.html")

    # membuat graph
    G = nx.Graph()
    for i in range(len(nodes)):
        G.add_node(nodes[i])
        for j in range(i+1, len(nodes)):
            if graph[i][j] != 0:
                G.add_edge(nodes[i], nodes[j], weight=graph[i][j])
    
    # mengatur warna dan label untuk nodes
    nodeColors = []
    nodeLabels = {}
    for node in G.nodes():
        if node in path:
            nodeColors.append('#d3b2d9')
        else:
            nodeColors.append('#b2d3d9')
        nodeLabels[node] = node
    
    # mengatur warna dan label untuk edges
    edgeColors = []
    edgeLabels = {}
    for u, v, data in G.edges(data=True):
        if (u in path and v in path):
            edgeColors.append('#5e2d61')
        else:
            edgeColors.append('black')
        edgeLabels[(u,v)] = data['weight']
    
    # plotting graph dengan warna dan label 
    pos = {nodes[i]: coordinates[i][::-1] for i in range(len(nodes))}
    nx.draw_networkx_nodes(G, pos, node_color=nodeColors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color=edgeColors)
    nx.draw_networkx_labels(G, pos, nodeLabels, font_size=8, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edgeLabels, font_size=8, font_weight='bold')
    plt.show()

def showMap(nodes, graph, path, coordinates):
    avgLat = sum([coordinates[i][0] for i in range(len(coordinates))]) / len(coordinates)
    avgLng = sum([coordinates[i][1] for i in range(len(coordinates))]) / len(coordinates)
    gmap = gmplot.GoogleMapPlotter(avgLat, avgLng, apikey="AIzaSyB5UAh67qqEWkt8i2VH6AMD3KJgIdx4vNI", use_api=True, map_type="roadmap", zoom=14, title="Shortest Path")

    # Plotting semua nodes
    for i, node in enumerate(nodes):
        lat, lng = coordinates[i]
        gmap.marker(lat, lng, title=node)

    # Plotting semua edges
    for i in range(len(graph)):
        for j in range(i+1, len(graph)):
            if graph[i][j] != 0:
                lat1, lng1 = coordinates[i]
                lat2, lng2 = coordinates[j]
                if (nodes[i] in path and nodes[j] in path):
                    gmap.plot([lat1, lat2], [lng1, lng2], 'red', edge_width=5)
                else:
                    gmap.plot([lat1, lat2], [lng1, lng2], 'blue', edge_width=5)

    # Menampilkan map dalam file html
    gmap.draw("bin/map.html")