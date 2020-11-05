def DFS(x):
    Q = []
    Q.append(x)
    visit[x] = 1
    while Q:
        y = Q.pop()
        for i in tmp[y]:
            if visit[i] == 0:
                visit[i] = 1
                Q.append(i)
    return

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = [[]for _ in range(N+1)]
    visit = [0]*(N+1)
    for i in range(0, len(arr), 2):
        tmp[arr[i]].append(arr[i + 1])
        tmp[arr[i + 1]].append(arr[i])
    cnt = 0
    for i in range(1, len(tmp)):
        if not tmp:
            cnt += 1
        else:
            if visit[i] == 0:
                DFS(i)
                cnt += 1
    print('#{} {}'.format(tc, cnt))