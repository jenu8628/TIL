import sys
from collections import deque

MAX = 10 ** 5
dist = [0] * (MAX + 1)
N, K = map(int, sys.stdin.readline().split())
Q = deque([N])
while Q:
    x = Q.popleft()
    if x == K:
        print(dist[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and not dist[nx]:
            dist[nx] = dist[x] + 1
            Q.append(nx)