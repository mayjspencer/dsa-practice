import heapq

def dijkstra(graph, start):
    # Min-heap priority queue initialized with the start node and distance 0
    heap = [(0, start)]

    # Dictionary to store the shortest known distance to each node
    distances = {}

    # Set to keep track of visited nodes so we don't revisit them
    visited = set()

    # Process the heap until there are no more nodes to evaluate
    while heap:
        # Get the node with the smallest distance so far
        curr_dist, node = heapq.heappop(heap)

        # Skip if we've already finalized the shortest path to this node
        if node in visited:
            continue

        # Mark the node as visited and record its shortest distance
        visited.add(node)
        distances[node] = curr_dist

        # Explore neighbors of the current node
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                # Add the neighbor to the heap with updated total distance
                heapq.heappush(heap, (curr_dist + weight, neighbor))

    # Return the computed shortest distances from the start node
    return distances


# --- 🔎 Example Test Case ---
if __name__ == "__main__":
    graph = {
        'A': [('B', 5), ('C', 2)],
        'B': [('D', 1)],
        'C': [('B', 8), ('D', 7)],
        'D': []
    }

    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)

    print(f"Shortest paths from {start_node}:")
    for node in sorted(shortest_paths):
        print(f"  {node}: {shortest_paths[node]}")
