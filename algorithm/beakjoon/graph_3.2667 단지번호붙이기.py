import sys
from collections import deque

def bfs(r, c):
    Q = deque([(r, c)])
    arr[r][c] = 0
    cnt = 1
    while Q:
        dr, dc = Q.popleft()
        for i in range(4):
            nr = dr + d[i][0]
            nc = dc + d[i][1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '1':
                arr[nr][nc] = 0
                Q.append((nr, nc))
                cnt += 1
    return cnt

N = int(sys.stdin.readline())
arr = []
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(N):
    temp = list(input())
    arr.append(temp)
visit = [[0]*N for _ in range(N)]
ans = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == '1':
            ans.append(bfs(r, c))
print(len(ans))
for i in sorted(ans):
    print(i)