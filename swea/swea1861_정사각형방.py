import sys
sys.stdin = open('sample_input(1).txt', 'r')

# 내풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def dfs(r, c):
    global cnt
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            continue
        if squ[r][c] + 1 == squ[nr][nc]:
            cnt += 1
            dfs(nr, nc)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    squ = [list(map(int, input().split())) for _ in range(N)]
    total = []
    for i in range(N):
        for j in range(N):
            cnt = 1
            dfs(i, j)
            total.append([i, j, cnt])
    # 가장 작은 횟수 찾기
    max_number = 0
    for k in range(len(total)):
        if total[k][2] > max_number:
            max_number = total[k][2]
    # 이동할 수 있는 방의 개수가 최대인 방의
    # squ의 값을 idx에 추가
    idx = []
    for n in range(len(total)):
        if total[n][2] == max_number:
            idx.append((squ[total[n][0]][total[n][1]]))
    print('#{} {} {}'.format(tc, min(idx), max_number))

# 하영이풀이
T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x):
    global cnt

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and sq[ny][nx] == sq[y][x] + 1:
            cnt += 1
            dfs(ny, nx)
    return cnt

for tc in range(1, T + 1):
    N = int(input())
    sq = [list(map(int, input().split())) for _ in range(N)]
    res = []
    for y in range(N):
        for x in range(N):
            cnt = 1
            res.append([sq[y][x], dfs(y, x)])
    res = sorted(res, key=lambda x: (-x[1], x[0]))
    print('#{} {} {}'.format(tc, res[0][0], res[0][1]))

# 쌤풀이
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(stR,stC):
    global ans_num, ans_dist
    queue = [(stR, stC)]
    cnt = 0
    while queue:
        r, c = queue.pop(0)
        cnt += 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if arr[nr][nc] - arr[r][c] == 1:
                queue.append((nr, nc))

    if cnt >= ans_dist:
        if cnt == ans_dist:
            ans_num = min(ans_num, arr[stR][stC])
        else:
            ans_num = arr[stR][stC]

        ans_dist = cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+2) for _ in range((N+2))]
    for i in range(1, N+1):
        tmp = list(map(int, input().split()))
        for j in range(1, N+1):
            arr[i][j] = tmp[j-1]

    ans_dist = 0
    ans_num = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            BFS(i,j)
    print("#{} {} {}".format(tc, ans_num, ans_dist))

# 쌤풀이 2
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dist = [1] * (N*N+1) #거리
    num = [0] * (N*N+1)

    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            # 해당 빈 인덱스에 좌표 넣기
            num[arr[i][j]] = (i,j)

    # 2번부터 끝번호까지 수행
    for i in range(2, N*N +1):
        for d in range(4):
            # 다음 좌표확인
            # num[i][0] = 행, [1] = 열
            nr = num[i][0] + dr[d]
            nc = num[i][1] + dc[d]
            # 범위안에 들어오면서, 다음자리가 현재 내 방번호보다 하나 작다면
            if 0<= nr < N and 0<=nc < N and i - 1 == arr[nr][nc]:
                # 현재방은 전방 +1 거리만큼 이동가능
                dist[i] = dist[i-1] + 1
                break

    ans_num, ans_dist = N*N, 0
    for i in range(1, N*N+1):
        if dist[i] > ans_dist:
            ans_num = i
            ans_dist = dist[i]

    print("#{} {} {}".format(tc, ans_num-(ans_dist-1), ans_dist))