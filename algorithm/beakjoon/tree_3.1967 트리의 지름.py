import sys
from collections import deque

def bfs(x, mode):
    Q = deque([x])
    dist = [-1 for _ in range(N+1)]
    dist[x] = 0
    while Q:
        a = Q.popleft()
        for child, weight in tree[a]:
            if dist[child] == -1:
                dist[child] = dist[a] + weight
                Q.append(child)
    if mode == 1:
        return dist.index(max(dist))
    else:
        return max(dist)


N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])
print(bfs(bfs(1, 1), 2))
