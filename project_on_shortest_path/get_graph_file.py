def get_graph():
    graph = {}
    nodes = input("Enter the nodes (separated by spaces): ").upper()
    nodes = nodes.split()
    for node in nodes:
        edges_list = []
        print(f"Enter edges for node {node}:")
        while True:
            edge_node = input("Enter edge node (or leave blank to stop): ").upper()
            if edge_node == "":
                break
            if edge_node not in nodes:
                print(f"Node {edge_node} is not in the list of nodes. Skipping...")
                continue
            edge_cost = int(input(f"Enter edge cost for node {edge_node}: "))
            edges_list.append((edge_node, edge_cost))
            print(f"Edge {node} - {edge_node} added with cost {edge_cost}")
        graph[node] = edges_list
        print("\n")
        print_graph(graph)
    return graph

def print_graph(graph):
    print("Graph:")
    for node, edges in graph.items():
        print(f"{node}: ", end="")
        for neighbor, cost in edges:
            print(f"{neighbor} ({cost})", end=" ")
        print()




