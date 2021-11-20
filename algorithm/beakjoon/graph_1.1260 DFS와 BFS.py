from collections import deque

def bfs(x):
    Q = deque([x])
    visit = [x]
    ans = [x]
    while Q:
        start = Q.popleft()
        print(start, end=" ")
        for end in arr[start]:
            if end not in visit:
                Q.append(end)
                visit.append(end)
    return ans

def dfs(x):
    visited[x] = 1
    print(x, end=" ")
    for end in arr[x]:
        if visited[end] == 0:
            dfs(end)

N, M, V = map(int, input().split())
arr = {i: [] for i in range(N+1)} # 인접 리스트
# arr = [[0]*(N+1) for _ in range(N+1)] # 인접행렬
for i in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
for i in range(1, N+1):
    arr[i].sort()
visited = [0]*(N+1)
dfs(V)
print()
bfs(V)
