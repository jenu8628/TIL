import sys
from collections import deque

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(r, c):
    Q = deque([(r,c)])
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nr = x + d[i][0]
            nc = y + d[i][1]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                Q.append((nr, nc))
                arr[nr][nc] = 0

for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        c, r = map(int, sys.stdin.readline().split())
        arr[r][c] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                ans += 1
                bfs(i, j)
    print(ans)