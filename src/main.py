from readFile import *
from ucs import *
from astar import *
from visualize import *

def main():
    print("Welcome to the Path Finder!")
    print("Please choose the algorithm you want to use:")
    print("1. Uniform Cost Search")
    print("2. A* Search")
    print("3. Exit")
    choice = input("Your choice: ")
    if choice == '1':
        filename = input("Please enter the filename: ")
        nodes, graph = readFileUCS(filename)
        start = input("Please enter the start node: ")
        goal = input("Please enter the goal node: ")
        path, cost = ucs(graph, start, goal, nodes)
        printPath(path, cost)
        show = input("Do you want to see the graph? (y/n): ")
        if show == 'y':
            showGraphUCS(nodes, graph, path)
        else:
            print("Thank you for using our program!")
    elif choice == '2':
        filename = input("Please enter the filename: ")
        nodes, graph, coordinates = readFileAStar(filename)
        start = input("Please enter the start node: ")
        goal = input("Please enter the goal node: ")
        path, cost = aStar(start, goal, nodes, graph, coordinates)
        printPath(path, cost)
        show = input("Do you want to see the graph? (y/n): ")
        if show == 'y':
            showGraphAStar(nodes, graph, path, coordinates)
        else:
            print("Thank you for using our program!")

if __name__ == "__main__":
    main()