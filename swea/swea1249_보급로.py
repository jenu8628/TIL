dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# from collections import deque

for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    dist = [[987654321]*n for _ in range(n)]
    dist[0][0] = 0
    bfs(0, 0)
    print('#{} {}'.format(tc, dist[n-1][n-1]))