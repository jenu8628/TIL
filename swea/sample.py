def dfs(x, y):
    visited[x][y] = 1
    global cnt
    if x == 99:
        return

    for i in range(3):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < 100 and 0 <= my < 100:
            if not visited[mx][my] and arr[mx][my] == 1:
                cnt += 1
                return dfs(mx, my)

for i in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dx = [0, 0, 1]
    dy = [1, -1, 0]
    result = []
    total = []
    for j in range(100):
        cnt = 0
        visited = [[0] * 100 for _ in range(100)]
        if arr[0][j] == 1:
            dfs(0, j)
            result.append(cnt)
        total.append(cnt)
    min_index = total.index(min(result))
    print('#{} {}'.format(tc, min_index))