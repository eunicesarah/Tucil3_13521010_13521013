filename = input("Enter the name of the file you want to read: ")
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        graph = [[int(num) for num in line.split()] for line in file]
    return graph

graph = read_graph_from_file(filename)
print(graph)