import pprint
from get_graph_file import get_graph
from shortest_path_finder import shortest_path

def options():
    options_list = {
        '1': 'Enter a new graph',
        '2': 'Find the shortest path in the graph',
        '3': 'Exit'
    }
    print(pprint.pformat(options_list))
    choice = int(input('Please enter your option (1/2/3): '))
    return choice

def main():
    graph = {}
    while True:
        choice = options()
        if choice == 1:
            graph = get_graph()
        elif choice ==2:
            if graph is {}:
                print("No graph loaded. Please load a graph first.")
            else:
                start = input("Enter the start node: ").upper()
                end = input("Enter the end node: ").upper()
                if start in graph and end in graph:
                    shortest_path(graph, start, end)
                else:
                    print("One or both of the nodes entered are not present in the graph.")
        elif choice ==3:
            print("Exiting Program...")
            break
        else:
            print('Invalid Option')

if __name__ == "__main__":
    main()
