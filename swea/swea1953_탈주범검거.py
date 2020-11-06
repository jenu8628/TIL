dr = [[0], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
dc = [[0], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]

# from collections import deque

for tc in range(1, int(input()) + 1):
    # N:세로크기, M:가로크기 R: 맨홀뚜껑세로위치 C: 맨홀가로위치 L:소요된시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*(M+1) for _ in range(N+1)]
    # Q = deque()
    # Q.append((R, C, 1))
    Q = [(R, C, 1)]
    visit[R][C] = 1
    idx = -1
    cnt = 1
    while Q:
        # r, c, t = Q.popleft()
        idx += 1
        if idx == len(Q):
            break
        r, c, t = Q[idx]
        if t == L:
            break
        for i in range(len(dr[arr[r][c]])):
            nr = r + dr[arr[r][c]][i]
            nc = c + dc[arr[r][c]][i]
            if nr < 0 or nr > N - 1 or nc < 0 or nc > M-1 or arr[nr][nc] == 0:
                continue
            for j in range(len(dr[arr[nr][nc]])):
                ar = nr + dr[arr[nr][nc]][j]
                ac = nc + dc[arr[nr][nc]][j]
                if r == ar and c == ac:
                    if visit[nr][nc] == 0:
                        Q.append((nr, nc, t + 1))
                        visit[nr][nc] = 1
                        cnt += 1
                    break
    print('#{} {}'.format(tc, cnt))