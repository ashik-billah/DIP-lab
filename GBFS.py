import heapq  # for priority queue

def greedy_bfs(graph,start,goal,h):
    visited = set()
    pq = []
    parent = {}
    cost = {}
    heapq.heappush(pq,(h[start],start))
    parent[start] = None
    cost[start] = 0

    while pq:
        _,node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            print("Cost",cost[goal])
            return path[::-1]
        for nei,c in graph.get(node,[]):
            nc = cost[node] + c
            if nei  not in visited:
                parent[nei] = node
                cost[nei] = nc
                heapq.heappush(pq,(h[nei],nei))
    return None

graph = {
    'S': [('A', 3), ('B', 2)],
    'A': [('S', 3), ('C', 4), ('D', 2)],
    'B': [('S', 2), ('E', 5), ('F', 1)],
    'C': [('A', 4)],
    'D': [('A', 2)],
    'E': [('B', 5), ('G', 2)],
    'F': [('B', 1)],
    'G': [('E', 2)]
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 1,
    'C': 5,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}
path = greedy_bfs(graph, 'S', 'G', heuristic)
print("Actual Greedy BFS Path:", path)
