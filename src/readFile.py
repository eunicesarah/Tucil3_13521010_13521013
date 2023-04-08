import matplotlib.pyplot as plt 
import networkx as nx 

def read_graph_from_file(filename):
    with open('test/' + filename + '.txt', 'r') as file:
        graph = [[int(num) for num in line.split()] for line in file]
    return graph

def show_graph(graph):
    G = nx.DiGraph() 
    for i in range(len(graph)): 
        for j in range(len(graph[i])): 
            if graph[i][j] != 0: 
                G.add_edge(i,j) 
    nx.draw(G, with_labels = True, edge_color = 'black', node_color = '#bca0dc') 
    plt.show() 