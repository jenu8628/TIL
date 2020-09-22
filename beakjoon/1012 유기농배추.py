dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# def DFS(r, c):
#     arr[r][c] = 0
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M:
#             if arr[nr][nc] == 1:
#                 DFS(nr, nc)

def BFS(r,c):
    global visit
    visit.append((r, c))
    q = [(r, c)]
    while q:
        curr_r, curr_c = q.pop()
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 1 and (nr, nc) not in visit:
                    q.append((nr, nc))
                    visit.append((nr, nc))

T = int(input())
for tc in range(T):
    # M : 가로길이, N : 세로길이, K : 배추가 심어져 있는 개수
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visit = []
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 or (i,j) in visit:
                continue
            else:
                cnt += 1
                # DFS(i, j)
                BFS(i, j)
    print(cnt)