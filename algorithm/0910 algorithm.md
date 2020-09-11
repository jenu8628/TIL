### swea7465 _ 창용마을 무리의 개수

```python
# 풀이 1
def dfs(x):
    q.append(x)
    for w in visit[x]:
        if w not in q:
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    visit = [[] for _ in range(N+1)]
    q = []
    for i in range(M):
        st, ed = map(int, input().split())
        visit[st].append(ed)
        visit[ed].append(st)

    for i in range(1, N+1):
        if i not in q:
            cnt += 1
            dfs(i)
    print('#{} {}'.format(tc, cnt))

# 풀이 2
def dfs(x):
    global cnt
    for i in range(1, N+1):
        if arr[x][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    count = 0
    lis = []
    visit = [0] * (N + 1)
    for i in range(M):
        st, ed = map(int, input().split())
        lis.append([st, ed])
        arr[st][ed] = arr[ed][st] = 1
    for i in lis:
        if visit[i[0]] == 0:
            count += 1
            dfs(i[0])
    for i in range(1,N+1):
        if visit[i] == 0:
            count += 1
    print('#{} {}'.format(tc, count))

# 풀이 3
for t in range(int(input())):
    n, m = map(int, input().split())
    a = [i for i in range(n+1)]
    for i in range(m):
        x, y = map(int, input().split())
        a = [a[x] if j == a[y] else j for j in a]
    print(f'#{t+1}', len(set(a[1:])))

# 쌤풀이
def BFS(v):
    queue = [v]
    visited[v] = 1
    while len(queue) > 0:
        # 큐에서 한명 꺼내기
        curr = queue.pop()
        for j in adj[curr]:
            if not visited[j]:
                visited[j] = 1
                queue.append(j)

def DFS(v):
    visited[v] = 1
    for i in adj[v]:
        if not visited[i]:
            DFS(i)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    #인접리스트
    adj = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    visited = [0] * (V+1)
    ans = 0
    for i in range(1, V+1):
        if visited[i] == 0:
            ans += 1
            BFS(i)
    print("#{} {}".format(tc, ans))
```



### swea1486_장훈이의 높은 선반

```python
# 풀이 1(조합) == 모든 조합을 뽑으면 부분집합
def comb(idx, sidx, R):
    if sidx == R:
        if sum(sel) >= B:
            total.append(sum(sel))
        return

    for j in range(idx, N):
        sel[sidx] = arr[j]
        comb(j+1, sidx+1, R)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    for i in range(1, N+1):
        sel = [0] * i
        comb(0, 0, i)
    print('#{} {}'.format(tc, min(total) - B))

# 풀이 2 부분집합
def powerset(idx):
    if idx == N :
        result = 0
        for i in range(N):
            if sel[i] == 1:
                result += arr[i]
        if result >= B:
            total.append(result)
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    sel = [0] * N
    powerset(0)
    print('#{} {}'.format(tc, min(total) - B))


# 쌤풀이
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 99999999999

    # 비트마스킹 형식으로 powerset
    for i in range(1, 1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += H[j]
        if total >= B and total < ans:
            ans = total
    print("#{} {}".format(tc, ans - B))
```



### swea1861_정사각형방

```python
import sys
sys.stdin = open('sample_input(1).txt', 'r')

# 내풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    global cnt
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if squ[r][c] + 1 == squ[nr][nc]:
            cnt += 1
            dfs(nr, nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    squ = [list(map(int, input().split())) for _ in range(N)]
    total = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j)
            total.append([i, j, cnt])
    # 가장 작은 횟수 찾기
    max_number = 0
    for k in range(len(total)):
        if total[k][2] > max_number:
            max_number = total[k][2]
    # 이동할 수 있는 방의 개수가 최대인 방의
    # squ의 값을 idx에 추가
    idx = []
    for n in range(len(total)):
        if total[n][2] == max_number:
            idx.append((squ[total[n][0]][total[n][1]]))
    print('#{} {} {}'.format(tc, min(idx), max_number))

# 쌤풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(stR,stC):
    global ans_num, ans_dist
    queue = [(stR, stC)]
    cnt = 0
    while queue:
        r, c = queue.pop(0)
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if arr[nr][nc] - arr[r][c] == 1:
                queue.append((nr, nc))

    if cnt >= ans_dist:
        if cnt == ans_dist:
            ans_num = min(ans_num, arr[stR][stC])
        else:
            ans_num = arr[stR][stC]

        ans_dist = cnt

# 쌤풀이 2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+2) for _ in range((N+2))]
    for i in range(1, N+1):
        tmp = list(map(int, input().split()))
        for j in range(1, N+1):
            arr[i][j] = tmp[j-1]

    ans_dist = 0
    ans_num = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            BFS(i,j)
    print("#{} {} {}".format(tc, ans_num, ans_dist))
    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dist = [1] * (N*N+1) #거리
    num = [0] * (N*N+1)

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            # 해당 빈 인덱스에 좌표 넣기
            num[arr[i][j]] = (i,j)

    # 2번부터 끝번호까지 수행
    for i in range(2, N*N +1):
        for d in range(4):
            # 다음 좌표확인
            # num[i][0] = 행, [1] = 열
            nr = num[i][0] + dr[d]
            nc = num[i][1] + dc[d]
            # 범위안에 들어오면서, 다음자리가 현재 내 방번호보다 하나 작다면
            if 0<= nr < N and 0<=nc < N and i - 1 == arr[nr][nc]:
                # 현재방은 전방 +1 거리만큼 이동가능
                dist[i] = dist[i-1] + 1
                break

    ans_num, ans_dist = N*N, 0
    for i in range(1, N*N+1):
        if dist[i] > ans_dist:
            ans_num = i
            ans_dist = dist[i]

    print("#{} {} {}".format(tc, ans_num-(ans_dist-1), ans_dist))
```



### swea1231_중위순회

```python
def inOrder(v):
    # 왼쪽 자식이 있을 때
    if len(arr[v]) >= 3 :
        inOrder(int(arr[v][2]))
    # 출력
    print(arr[v][1], end = "")
    # 오른쪽 자식이 있을 때
    if len(arr[v]) ==4:
        inOrder(int(arr[v][3]))

for tc in range(1,11):
    N = int(input())

    # 2차원리스트로 인접리스트느낌으로 처리
    arr = [[]] # 0번인덱스 버리기기

    for i in range(N):
        arr.append(input().split())

    print("#{}".format(tc), end=" ")
    inOrder(1)
    print()
```



### swea1267_작업순서

```python
# 내풀이
def bfs(x):
    q = []
    q.append(x)
    visited = [0] * (V+1)
    total.append(x)
    while len(q):
        curr = q.pop(0)
        for w in range(1, V+1):
            if arr[curr][w] == 1 and visited[w] == 0:
                if visit[w] == 1:
                    total.append(w)
                    q.append(w)
                    visited[w] = 1
                else:
                    visit[w] -= 1

for tc in range(1, 11):
    V, E = map(int, input().split())
    lis = list(map(int, input().split()))
    arr = [[0] * (V+1) for _ in range(V+1)]
    visit = [0] * (V+1)
    total = []
    for i in range(E):
        st, ed = lis[2*i], lis[2*i+1]
        arr[st][ed] = 1
        visit[ed] += 1
    for j in range(1, len(visit)):
        if visit[j] == 0:
            bfs(j)
    print('#{}'.format(tc), end=' ')
    for i in total:
        print(i, end=' ')
    print()

# 쌤풀이
for tc in range(1, 11):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))
    prev_arr = [[0]*(V+1) for _ in range(V+1)]
    order = []
    work = [0] * (V+1)
    for i in range(0, len(edges), 2):
        st, ed = edges[i], edges[i+1]
        prev_arr[ed][st] = 1

    # 선행작없이 하나도 없는 일은 미리 담아두자
    for i in range(1, len(prev_arr)):
        if prev_arr[i].count(1) == 0:
            order.append(i)
            work[i] = 1

    # 작업을 할 차례
    while len(order) != V:
        for i in range(1, V+1):
            # 해당 작업을 안했다.
            if work[i] == 0:
                # 선행작업을 확인
                for j in range(1, V+1):
                    # 선행작업이 있네?
                    if prev_arr[i][j] == 1:
                        # 그거 안했어? 그러면 break
                        if work[j] == 0:
                            break
                # 조기 브레이크 안걸렸어? 그러면 일 해~
                else:
                    order.append(i)
                    work[i] = 1
    print("#{}".format(tc), end = " ")
    for i in order:
        print(i, end=" ")
    print()

# 쌤풀이 2
def DFS(v):
    work[v] = 1 # 노드 방문을 했으니, 작업 했음을 표시
    for w in adj[v]: # 해당 작업의 후행 작업 순회
        if not work[w]: # 해당 작업을 하지 않았으면 수행
            DFS(w)
    stack.append(v)

for tc in range(1, 11):
    V, E = map(int, input().split())
    # 인접리스트
    adj = [[] for _ in range(V+1)]
    work = [0] * (V+1) # 일을 했는지 안했는지
    count = [0] * (V+1) # 선행작업 카운트
    stack = []
    edge = list(map(int, input().split()))
    for i in range(0, E):
        st, ed = edge[i*2], edge[i*2+1]
        adj[st].append(ed)
        count[ed] += 1 # 선행작업 개수 증가
    for i in range(1, V+1):
        if count[i] == 0: # 선행 작업이 없는 노드 먼저 시작!
            DFS(i)

    print("#{}".format(tc), end =" ")
    print(*stack[::-1])
```

