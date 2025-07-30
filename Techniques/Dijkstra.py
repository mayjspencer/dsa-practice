import heapq

def dijkstra(graph, start):
    # Min-heap: (distance_so_far, current_node)
    heap = [(0, start)]
    distances = {}
    visited = set()

    while heap:
        curr_dist, node = heapq.heappop(heap)

        if node in visited:
            continue

        visited.add(node)
        distances[node] = curr_dist

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(heap, (curr_dist + weight, neighbor))

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
