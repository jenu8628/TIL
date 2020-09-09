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