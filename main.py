import heapq


def prim(graph, start):
    visited = {start}
    edges = []
    total_weight = 0
    minimum_spanning_tree = []

    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))

    while edges and len(visited) < len(graph):
        weight, source, destination = heapq.heappop(edges)

        if destination in visited:
            continue

        visited.add(destination)
        minimum_spanning_tree.append((source, destination, weight))
        total_weight += weight

        for neighbor, next_weight in graph[destination]:
            if neighbor not in visited:
                heapq.heappush(edges, (next_weight, destination, neighbor))

    return minimum_spanning_tree, total_weight


if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }
    mst, cost = prim(graph, "A")
    print("MST:", mst)
    print("Total weight:", cost)
