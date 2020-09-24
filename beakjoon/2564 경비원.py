dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def left(r, c):
    global cnt
    visit[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = r + dc[i]
        if 0 <= nr < Y and 0 <= nc < X:
            if arr[nr][nc] != 0 and visit[nr][nc] == 0:
                cnt += 1
                left(nr, nc)
                if arr[nr][nc] == 2:
                    arr[nr][nc] = 1
                    left_cnt.append(cnt)
                    return
def right(r,c):
    global cnt
    visit[r][c] = 2
    for i in range(3, -1, -1):
        nr = r + dr[i]
        nc = r + dc[i]
        if 0 <= nr < Y and 0 <= nc < X:
            if arr[nr][nc] != 0:
                if visit[nr][nc] == 0 or visit[nr][nc] == 1:
                    cnt += 1
                    if arr[nr][nc] == 2:
                        arr[nr][nc] = 1
                        right_cnt.append(cnt)

X, Y = map(int, input().split())
arr = [[1] + [0]*(X-2) + [1] for _ in range(Y-2)]
arr = [[1] * X] + arr + [[1] * X]
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    if a == 1:
        arr[0][b] = 2
    if a == 2:
        arr[Y-1][b] = 2
    if a == 3:
        arr[b][0] = 2
    else:
        arr[b][X-1] = 2
c, d = map(int, input().split())
left_cnt = []
right_cnt = []
for i in range(N):
    visit = [[0]*X for _ in range(Y)]
    left(c, d)
    right(c, d)
# for i in range(5):
#     for j in range(10):
#         cnt = 0
#         if arr[i][j] == 1:
#