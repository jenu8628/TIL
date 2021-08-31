def DFS(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, N+1):
        if arr[v][i] == 1 and visit[i] == 0:
            DFS(i)

def BFS(v):
    q = [v]
    visited = [v]
    while q:
        c = q.pop(0)
        print(c, end=' ')
        for i in range(N + 1):
            if arr[c][i] == 1 and i not in visited:
                q.append(i)
                visited.append(i)

N, M, V = map(int, input().split())
visit = [0] * (N + 1)
arr = [[0] * (N + 1) for _ in range(N+1)]
for i in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] = 1
DFS(V)
print()
BFS(V)