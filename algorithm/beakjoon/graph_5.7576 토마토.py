import sys
from collections import deque

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
M, N = map(int, sys.stdin.readline().split())
arr = []
Q = deque([])

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    arr.append(temp)
    if 1 in temp:
        for j in range(len(temp)):
            if arr[i][j] == 1:
                Q.append((i, j))
ans = 0
while Q:
    r, c = Q.popleft()
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            Q.append((nr, nc))
            arr[nr][nc] = arr[r][c] + 1
flag = False
for i in arr:
    for j in i:
        if j == 0:
            flag = True
            break
        else:
            ans = max(ans, j)
    if flag:
        print(-1)
        break
if not flag:
    print(ans - 1)