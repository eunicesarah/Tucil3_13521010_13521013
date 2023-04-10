import matplotlib.pyplot as plt 
import networkx as nx 

def read_graph_from_file(filename):
    try:
        with open('test/' + filename + '.txt', 'r') as file:
            graph = [[int(num) for num in line.split()] for line in file]
            if len(graph) == 0:
                raise ValueError("File is empty!")
            elif len(graph) != len(graph[0]):
                raise ValueError("Graph must be square!")
            else:
                for i in range(len(graph)):
                    for j in range(len(graph)):
                        if graph[i][i] != 0:
                            raise ValueError(f"Diagonal elements graph[{i}][{i}] must be 0!")
                        if graph[i][j] != graph[j][i]:
                            raise ValueError(f"Graph[{i}][{j}] must be equal to graph[{j}][{i}]!]")
        return graph
    except FileNotFoundError:
        print(f"File {filename}.txt not found!")
    except ValueError as e:
        print(str(e))

def show_graph(graph):
    G = nx.DiGraph() 
    for i in range(len(graph)): 
        for j in range(len(graph[i])): 
            if graph[i][j] != 0: 
               G.add_edge(i,j, weight=graph[i][j]) # menambahkan bobot pada setiap edge
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True, edge_color='black', node_color='#bca0dc', font_size= 10, node_size= 500)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_size= 8) # menampilkan label pada setiap edge
    # mengambil manajer gambar saat ini
    mgr = plt.get_current_fig_manager()

    # menampilkan grafik dalam mode fullscreen
    mgr.full_screen_toggle()
    plt.show()