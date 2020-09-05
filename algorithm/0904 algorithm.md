## SWEA문제

### 회전

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        x = arr.pop(0)
        arr.append(x)
    print("#{} {}".format(tc, arr[0]))
```



### 피자굽기

```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Q = []
    last = 0
    for j in range(M):
        C[j] = [j+1, C[j]]
    for i in range(1, N+1):
        Q.append(C.pop(0))

    while len(Q) > 0:
        if len(Q) == 1:
            last = Q.pop(0)
            break
        x = Q.pop(0)
        z = [x[0], x[1]//2]
        if z[1] == 0:
            if len(C) == 0:
                continue
            y = C.pop(0)
            Q.append(y)
            continue
        Q.append(z)
    print("#{} {}".format(tc, last[0]))
```



### 노드의 거리

```python
def BFS(x):
    global total
    visit[x] = 1
    Q = []
    Q.append(x)
    while Q:
        curr = Q.pop(0)
        for w in range(1, V+1):
            if arr[curr][w] == 1 and visit[w] == 0:
                Q.append(w)
                visit[w] = visit[curr] + 1
                if w == G:
                    total = visit[w] - 1
                    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    visit = [0] * (V+1)
    total = 0
    for i in range(E):
        st, ed = map(int, input().split())
        arr[st][ed] = arr[ed][st] = 1
    S, G = map(int, input().split())
    BFS(S)
    print("#{} {}".format(tc, total))
```



### 미로의 거리

```python
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    global total
    Q = []
    Q.append((r, c))
    visit[r][c] = 1
    while len(Q) != 0:
        curr_r, curr_c = Q.pop(0)
        for k in range(4):
            nr = curr_r + dr[k]
            nc = curr_c + dc[k]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if visit[nr][nc] != 0 or arr[nr][nc] == 1:
                continue
            Q.append((nr, nc))
            visit[nr][nc] = visit[curr_r][curr_c] + 1
            if arr[nr][nc] == 3:
                total = visit[nr][nc] - 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2 and visit[i][j] == 0:
                BFS(i, j)
                break
    print('#{} {}'.format(tc, total))
```







