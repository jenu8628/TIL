import heapq
import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = {i+1: {} for i in range(V)}

for _ in range(E):
    r, c, dist = map(int, sys.stdin.readline().split())
    if c in graph[r]:
        graph[r][c] = min(graph[r][c], dist)
        continue
    graph[r][c] = graph[r].get(c, dist)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        c_dist, c_node = heapq.heappop(queue)
        if distances[c_node] < c_dist:
            continue

        for idx, weight in graph[c_node].items():
            distance = c_dist + weight
            if distance < distances[idx]:
                distances[idx] = distance
                heapq.heappush(queue, [distance, idx])
    return distances

answer = dijkstra(graph, K)

for key, val in answer.items():
    if val == float('inf'):
        print('INF')
    else:
        print(val)
