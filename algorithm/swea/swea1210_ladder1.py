def dfs(x,y):
    visited[x][y] = True
    global result

    if x == 0:
        result = y
        return

    for i in range(3):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < 100 and 0 <= my < 100:
            if not visited[mx][my] and arr[mx][my] == 1:
                return dfs(mx, my)

for i in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    #밑에서부터 위로 올라가기
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    visited = [[0]*100 for _ in range(100)]
    x, y = 99, arr[99].index(2)
    result = -1
    dfs(x, y)
    print('#{} {}'.format(tc, result))