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

#하영이풀이
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