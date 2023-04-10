from readFile import read_graph_from_file
from coba import ucs
from astar import AStar
# from readFile import show_graph
import matplotlib.pyplot as plt 
import networkx as nx 

filename = input("Enter the name of the file you want to read: ")
graph = read_graph_from_file(filename)
while graph == None:
    filename = input("Enter the name of the file you want to read: ")
    read_graph_from_file(filename)
else:
    start = int(input("Enter the start node: "))
    goal = int(input("Enter the goal node: "))
    pathUCS, costUCS = ucs(graph, start, goal)
    # pathAstar, costAStar = AStar(graph, start, goal)
    print("Path from UCS: ", pathUCS)
    print("Cost from UCS: ", costUCS)
    # print("Path from A*: ", pathAstar)
    # print("Cost from A*: ", costAStar)
    showGraph = input("Do you want to see the graph? (y/n): ")
    if showGraph == 'y':
        G = nx.DiGraph() 
        for i in range(len(graph)): 
            for j in range(len(graph[i])): 
                if graph[i][j] != 0: 
                    G.add_edge(i,j, weight=graph[i][j])  # menambahkan bobot pada setiap edge
        pos = nx.spring_layout(G)
        path_edges = list(zip(pathUCS, pathUCS[1:]))
        labels = nx.get_edge_attributes(G, 'weight')
        edge_colors = ['red' if edge in path_edges else 'black' for edge in G.edges()]
        node_colors = ['red' if node in path_edges else 'blue'  for node in G.nodes()]
        # nx.draw(G, pos=pos, with_labels=True, edge_color='black', node_color='#bca0dc', font_size= 10, node_size= 500)
        nx.draw_networkx_nodes(G, pos, node_color='#bca0dc', node_size=500)
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
        nx.draw_networkx_labels(G, pos, font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
        plt.axis('off')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_size= 8) # menampilkan label pada setiap edge
        # # mengambil manajer gambar saat ini
        # mgr = plt.get_current_fig_manager()

        # # menampilkan grafik dalam mode fullscreen
        # mgr.full_screen_toggle()
        plt.show()