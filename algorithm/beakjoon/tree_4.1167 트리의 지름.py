import sys
from collections import deque

def bfs(x, mode):
    Q = deque([x])
    dist = [-1 for _ in range(N+1)]
    dist[x] = 0
    while Q:
        v = Q.popleft()
        for child, weight in tree[v]:
            if dist[child] == -1:
                dist[child] = dist[v] + weight
                Q.append(child)
    if mode == 1:
        return dist.index(max(dist))
    else:
        return max(dist)

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    v = temp[0]
    w = temp[1:]
    for i in range(0, len(w)-1, 2):
        tree[v].append(w[i:i+2])
print(bfs(bfs(1, 1), 2))
