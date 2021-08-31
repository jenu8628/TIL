def DFS(v):
    global cnt
    visit[v] = 1
    for i in range(1, N+1):
        if arr[v][i] == 1 and visit[i] == 0:
            cnt += 1
            DFS(i)

N = int(input())
M = int(input())
visit = [0] * (N + 1)
arr = [[0] * (N + 1) for _ in range(N+1)]
cnt = 0
for i in range(M):
    st, ed = map(int, input().split())
    arr[st][ed] = arr[ed][st] = 1
DFS(1)
print(cnt)