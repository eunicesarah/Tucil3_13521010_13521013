import networkx as nx
import matplotlib.pyplot as plt

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

def showGraphUCS(nodes, graph, path):
    G = nx.Graph()
    for i in range(len(nodes)):
        G.add_node(nodes[i])
        for j in range(i+1, len(nodes)):
            if graph[i][j] != 0:
                G.add_edge(nodes[i], nodes[j], weight=graph[i][j])
    
    # set color and labels for nodes
    node_colors = []
    node_labels = {}
    for node in G.nodes():
        if node in path:
            node_colors.append('#d3b2d9')
        else:
            node_colors.append('#b2d3d9')
        node_labels[node] = node
    
    # set color and labels for edges
    edge_colors = []
    edge_labels = {}
    for u, v, data in G.edges(data=True):
        if (u in path and v in path):
            edge_colors.append('#5e2d61')
        else:
            edge_colors.append('black')
        edge_labels[(u,v)] = data['weight']
    
    # plot graph with colors and labels
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_labels(G, pos, node_labels, font_size=8, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    plt.show()

def showGraphAStar(nodes, graph, path, coordinates):
    G = nx.Graph()
    for i in range(len(nodes)):
        G.add_node(nodes[i])
        for j in range(i+1, len(nodes)):
            if graph[i][j] != 0:
                G.add_edge(nodes[i], nodes[j], weight=graph[i][j])
    
    # set color and labels for nodes
    node_colors = []
    node_labels = {}
    for node in G.nodes():
        if node in path:
            node_colors.append('#d3b2d9')
        else:
            node_colors.append('#b2d3d9')
        node_labels[node] = node
    
    # set color and labels for edges
    edge_colors = []
    edge_labels = {}
    for u, v, data in G.edges(data=True):
        if (u in path and v in path):
            edge_colors.append('#5e2d61')
        else:
            edge_colors.append('black')
        edge_labels[(u,v)] = data['weight']
    
    # plot graph with colors and labels
    pos = {nodes[i]: coordinates[i] for i in range(len(nodes))}
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
    nx.draw_networkx_labels(G, pos, node_labels, font_size=8, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)
    plt.show()