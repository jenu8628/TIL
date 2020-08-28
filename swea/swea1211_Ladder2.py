# 내풀이
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

# 쌤 풀이(반복문)
dc = [-1, 1]
def dir_check(r, c):
    for i in range(2):
        nc = c + dc[i]
        if 0<= nc < 100 and ladder[r][nc] == 1:
            return i
    return 2

def go(st):
    col = st_pos[st]
    cnt = 0
    idx = st
    for i in range(100):
        d = dir_check(i, col)
        if d < 2 :
            idx += dc[d]
            cnt += abs(col - st_pos[idx])
            col = st_pos[idx]
        cnt += 1
    return cnt


for tc in range(10):
    # 테스트 케이스 번호 입력
    tc_num = int(input())
    # 2차원 리스트 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 시작 좌표를 담을 리스트
    st_pos = []
    # 시작 좌표를 다 담았다.
    for i in range(100):
        if ladder[0][i] == 1:
            st_pos.append(i)
    # 임의의 큰값으로 초기화
    min_value = 987654321
    # 어차피 정답으로 사용될거니 안쓰이는 수 아무거나로 초기화
    ans_idx = -1
    for i in range(len(st_pos)):
        tmp = go(i)

        if tmp <= min_value:
            min_value = tmp
            ans_idx = st_pos[i]

    print("#{} {}".format(tc_num, ans_idx))