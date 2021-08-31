def DFS(flag, idx, value):
    global ans
    if flag == (1 << N) - 1:
        if ans > value:
            ans = value
        return
    if value >= ans:
        return
    for i in range(N):
        if flag & (1 << i):
            continue
        DFS(flag | 1 << i, idx+1, value + (arr[idx][i]))

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999999999999999999999999
    DFS(0, 0, 0)
    print('#{} {}'.format(tc, ans))