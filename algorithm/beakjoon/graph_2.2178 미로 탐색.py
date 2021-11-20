import sys
from collections import deque
d = [[-1,0], [0,1], [1,0], [0, -1]]
N, M = map(int, sys.stdin.readline().split())
arr = []
dict = [[0]* M for _ in range(N)]
for _ in range(N):
    arr.append(list(input()))
Q = deque([(0, 0)])
arr[0][0] = 1
while Q:
    r, c = Q.popleft()
    for i in range(4):
        nr = r + d[i][0]
        nc = c + d[i][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '1':
            Q.append([nr, nc])
            arr[nr][nc] = arr[r][c] + 1
print(arr[N-1][M-1])
