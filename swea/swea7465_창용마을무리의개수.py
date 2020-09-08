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
        print(a)
    print(f'#{t+1}',len(set(a[1:])))
