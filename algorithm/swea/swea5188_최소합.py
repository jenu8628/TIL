dr = [0, 1]
dc = [1, 0]

def dfs(r, c, cnt):
    if min(ans) < cnt:
        return
    if r == N - 1 and c == N - 1:
        ans.append(cnt)
        return
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < N and nc < N:
            dfs(nr, nc, cnt+arr[nr][nc])

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = [99999999999999999999999999999999999999999999999999999999]
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, min(ans)))