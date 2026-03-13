# Prim

## Complexity

- Time: O(E log E)
- Space: O(V + E)

## Problem Description

Prim's algorithm builds a minimum spanning tree for a connected weighted graph. Starting from one chosen vertex, it repeatedly adds the lightest edge that connects a visited vertex to an unvisited vertex until all vertices are included.

## Code

```python
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
```

## Algorithm Steps

1. Start from a chosen vertex and mark it as visited.
2. Push every edge leaving that start vertex into a min-heap.
3. Repeatedly remove the lightest edge from the heap.
4. If that edge leads to an already visited vertex, skip it.
5. Otherwise, add the edge to the minimum spanning tree, add its weight to the total cost, and mark the destination vertex as visited.
6. Push the destination vertex's outgoing edges to unvisited neighbors into the heap.
7. Continue until all vertices have been visited or no candidate edges remain.

## Explanation

This implementation uses a min-heap to always choose the lightest valid edge on the boundary between visited and unvisited vertices. That greedy rule is what makes Prim's algorithm correct for minimum spanning tree construction. The algorithm returns both the list of tree edges and the total weight of the resulting spanning tree.
