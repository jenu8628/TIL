# 하영이풀이
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 델다 입력 방식
    # d = [-1, 1, 0]
    # x, y = 0, 0
    # for i in d:
    #     for j in d:
    #         if i == j == 0:
    #             continue
    #         else:
    #             dx = x + i
    #             dy = y + j
    # 초기설정
    board = [[0] * N for _ in range(N)]
    mid = N // 2
    board[mid][mid] = 2
    board[mid - 1][mid - 1] = 2
    board[mid - 1][mid] = 1
    board[mid][mid - 1] = 1

    # 델타설정
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, -1, 0, 1]

    # 입력값 받기
    for i in range(M):
        x, y, z = map(int, input().split())
        x, y = x - 1, y - 1
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            reverse = []
            while True:
                if 0 > nx or 0 > ny or N - 1 < nx or N - 1 < ny:    # 모서리 나가는 애들
                    reverse = []
                    break
                elif board[nx][ny] == 0:
                    reverse = []
                    break
                elif board[nx][ny] == z:
                    break
                else:
                    reverse.append((nx, ny))
                nx += dx[j]
                ny += dy[j]
            for m, n in reverse:
                board[m][n] = z
        board[x][y] = z

    # 흑백 수 세기
    cnt1, cnt2 = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == 2:
                cnt2 += 1

    print('#{} {} {}'.format(tc, cnt1, cnt2))


import sys
sys.stdin = open('sample_input(1).txt', 'r')
# 내 풀이
# 8방향
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [1, 0, -1, -1, 1, -1, 0, 1]
# 흑돌
def DFS(r, c, j):
    nr = r + dr[j]
    nc = c + dc[j]
    global total
    if visited[r][c] == 1:
        return
    visited[r][c] = 1
    # 모서리 나가는 애들
    if 0 > nr or 0 > nc or N - 1 < nr or N - 1 < nc:
        total = []
        return
    # 0일 때
    elif arr[nr][nc] == 0:
        total = []
        return
    elif arr[nr][nc] == z:
        return
    else:
        total.append([nr, nc])
        DFS(nr, nc, j)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]
    a = N//2 - 1
    b = N//2
    # 흑백 기본위치 생성
    arr[a][a] = 2
    arr[a][b] = 1
    arr[b][b] = 2
    arr[b][a] = 1

    for i in range(M):
        y, x, z = map(int, input().split())
        y = y - 1
        x = x - 1
        arr[x][y] = z
        total = []
        for j in range(8):
            visited = [[0] * N for _ in range(N)]
            DFS(x, y, j)
            for k in total:
                m = k[0]
                n = k[1]
                arr[m][n] = z

    # 흑백 수 세기
    cnt1, cnt2 = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cnt1 += 1
            elif arr[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(tc, cnt1, cnt2))


# 쌤 풀이
# 8방향 델타
# 우, 우하, 하 좌하, 좌, 좌상, 상, 우상
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def init():
    mid = N // 2
    othello[mid][mid] = othello[mid + 1][mid + 1] = 2
    othello[mid + 1][mid] = othello[mid][mid + 1] = 1

def change(r,c, color):
    #새로운 좌표에 돌은 놓았다.
    othello[r][c] = color
    for i in range(8):
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]
            if nr <= 0 or nr >N or nc <=0 or nc>N:
                break
            if othello[nr][nc] == 0:
                break
            if othello[nr][nc] == color:
                while not(nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] = color
                break

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    othello = [[0] * (N + 1) for _ in range(N + 1)]
    init()
    for i in range(M):
        c, r, color = map(int, input().split())
        change(r,c, color)

    b_cnt = 0
    w_cnt = 0
    for i in range(N+1):
        b_cnt += othello[i].count(1)
        w_cnt += othello[i].count(2)
    print('#{} {} {}'.format(tc, b_cnt, w_cnt))