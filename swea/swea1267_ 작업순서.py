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