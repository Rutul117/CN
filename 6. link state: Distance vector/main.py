def bellman_ford(graph, source):
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    for i in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                new_distance = distance[node] + graph[node][neighbor]
                if new_distance < distance[neighbor]:
                    distance[neighbor], predecessor[neighbor] = new_distance, node

    for node in graph:
        for neighbor in graph[node]:
            assert distance[node] + graph[node][neighbor] >= distance[neighbor], "Negative cycle detected"

    return distance, predecessor
def print_routing_table(destination_nodes, next_hop, cost):
    print("{:<20} {:<20} {:<20}".format("Destination", "Next Hop", "Cost"))
    for destination in destination_nodes:
        print("{:<20} {:<20} {:<20}".format(destination, str(next_hop[destination]), str(cost[destination])))

# Rest of the code remains unchanged
graph = {
    'a': {'b': -1, 'c':  4},
    'b': {'c':  3, 'd':  2, 'e':  2},
    'c': {},
    'd': {'b':  1, 'c':  5},
    'e': {'d': -3}
}

result = bellman_ford(graph, 'a')

destination_nodes = sorted(result[0].keys())  # Assuming 'a' is the source node
next_hop = result[1]
cost = result[0]

print_routing_table(destination_nodes, next_hop, cost)
