import sys
from collections import deque

def bfs(x):
    Q = deque([x])
    visit.append(x)
    while Q:
        r = Q.popleft()
        for i in arr[r]:
            if i not in visit:
                visit.append(i)
                Q.append(i)


N, M = map(int, sys.stdin.readline().split())
arr = {i:[] for i in range(1, N + 1)}
visit = []
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)
ans = 0
for i in range(1, N+1):
    if i not in visit:
        ans += 1
        bfs(i)
print(ans)