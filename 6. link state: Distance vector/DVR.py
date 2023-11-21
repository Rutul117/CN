def initialize_nodes():
    return {
        "A": {"neighbors": {"B": 1, "C": 5}, "distance_vector": {}},
        "B": {"neighbors": {"A": 1, "C": 3}, "distance_vector": {}},
        "C": {"neighbors": {"A": 5, "B": 3}, "distance_vector": {}},
    }


def update_distance_vector(nodes):
    for node in nodes:
        for neighbor, cost in nodes[node]["neighbors"].items():
            if neighbor not in nodes[node]["distance_vector"] or nodes[node]["distance_vector"][neighbor] > cost + nodes[neighbor]["neighbors"][node]:
                nodes[node]["distance_vector"][neighbor] = cost + nodes[neighbor]["neighbors"][node]


def print_distance_vectors(nodes):
    for node in nodes:
        print(f"Node {node}'s Distance Vector: {nodes[node]['distance_vector']}")


def distance_vector_routing(nodes, iterations):
    for _ in range(iterations):
        update_distance_vector(nodes)
        print_distance_vectors(nodes)


if __name__ == "__main__":
    nodes = initialize_nodes()
    distance_vector_routing(nodes, 3)