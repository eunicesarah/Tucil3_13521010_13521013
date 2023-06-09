from readFile import *
from ucs import *
from astar import *
from visualize import *
import sys
import time

def main():
    while True:
        print("Welcome to the Path Finder!")
        print("Please choose the algorithm you want to use:")
        print("1. Uniform Cost Search")
        print("2. A* Search")
        print("Press any key to exit program")
        choice = input("Your choice: ")
        if choice == '1':
            while True:
                filename = input("Please enter the filename: ")
                nodes, graph, coordinates = readFile(filename)
                if nodes is None and graph is None:
                    continue
                print("The map is: ")
                print(nodes)
                start = input("Please enter the start node: ")
                goal = input("Please enter the goal node: ")
                if start not in nodes or goal not in nodes:
                    print("Start or goal node not found!")
                    continue
                path, cost = ucs(graph, start, goal, nodes)
                if path is None and cost is None:
                    print("No path found!")
                    continue
                else:
                    for i in range(len(path)):
                        path[i] = nodes[path[i]]
                    printPath(path, cost)
                    show = input("Do you want to see the graph? (y/n): ")
                    if show == 'y':
                        showGraph(nodes, graph, path, coordinates)
                        print("Thank you for using our program!")
                break
        elif choice == '2':
            while True:
                filename = input("Please enter the filename: ")
                nodes, graph, coordinates = readFile(filename)
                if nodes is None and graph is None:
                    continue
                print("The map is: ")
                print(nodes)
                start = input("Please enter the start node: ")
                goal = input("Please enter the goal node: ")
                if start not in nodes or goal not in nodes:
                    print("Start or goal node not found!")
                    continue
                path, cost = aStar(graph, start, goal, nodes, coordinates)
                if path is None and cost is None:
                    print("No path found!")
                    continue
                else:
                    for i in range(len(path)):
                        path[i] = nodes[path[i]]
                    printPath(path, cost)
                    show = input("Do you want to see the graph? (y/n): ")
                    if show == 'y':
                        showGraph(nodes, graph, path, coordinates)
                        print("Thank you for using our program!")
                break
        elif (choice != '1' and choice != '2'):
                print("Bye!")
                time.sleep(2)
                sys.exit()


if __name__ == "__main__":
    main()