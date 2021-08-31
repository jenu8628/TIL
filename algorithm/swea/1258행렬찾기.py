def search(row, col):
    global X
    global Y
    dx = [0, 0, 1]  # 우 좌 하
    dy = [1, -1, 0]
    mapp[row][col] = 0  # 다녀간곳은 0으로 바꿔줌 왔던 곳 중복으로 방문하는 것을 방지하기 위함
    for i in range(3):
        if 0 <= row + dx[i] < n and 0 <= col + dy[i] < n and mapp[row + dx[i]][col + dy[i]] != 0:
            if row + dx[i] - init_x + 1 >= X:  # 길이가 최대인 부분이 행렬의 세로 길이
                X = row + dx[i] - init_x + 1
            if col + dy[i] - init_y >= Y:  # 길이가 최대인 부분이 행렬의 가로 길이
                Y = col + dy[i] - init_y + 1
            search(row + dx[i], col + dy[i])
    return X, Y


T = int(input())
for t in range(T):
    n = int(input())
    mapp = []
    cnt = 0  # 행렬 개수 카운팅
    result = []
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    for y in range(n):
        for x in range(n):
            if mapp[x][y] != 0:  # 0이 아닌 부분이 있으면 탐색 시작할꺼임
                cnt += 1
                X = 0  # 결과값에 들어갈 행
                Y = 0  # 결과값에 들어갈 열
                init_x = x  # 최초행
                init_y = y  # 최초열
                result.append(search(x, y))
    sorted_result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    # sorted_result = sorted(result,key=itemgetter(0*1,0))
    print(f'#{t + 1}', cnt, end=" ")
    for i in range(len(sorted_result)):
        print(*sorted_result[i], end=" ")
    print()


# 쌤풀이
def search_size(r, c):
    r_cnt = 0
    c_cnt = 0

    for i in range(r, N + 2):
        if arr[i][c] == 0:
            break
        r_cnt += 1
    for j in range(c, N + 2):
        if arr[r][j] == 0:
            break
        c_cnt += 1

    ans.append([r_cnt, c_cnt])
    # 지나간 곳이므로 0으로 바꿔줌
    init(r, c, r_cnt, c_cnt)
# 지나간 곳은 0으로 바꿔주는 함수
def init(r, c, r_cnt, c_cnt):
    for i in range(r, r + r_cnt):
        for j in range(c, c + c_cnt):
            arr[i][j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [0] * (N + 2)
    arr[0] = arr[N + 1] = [0] * (N + 2)
    for i in range(N):
        arr[i + 1] = [0] + list(map(int, input().split())) + [0]
    ans = []

    for i in range(1, N + 2): # 0자리는 어차피 0
        for j in range(1, N + 2):
            if arr[i][j] != 0:
                search_size(i, j)
    # lambda는 익명함수 ans리스트에서 각각의 요소를 가져와서 뒤의 조건의 기준으로
    # 정렬을 하겠다.
    ans = sorted(ans, key=lambda x: ((x[0] * x[1]), x[0]))
    print("#{} {}".format(tc, len(ans)), end=" ")
    for i in range(len(ans)):
        print("{} {}".format(ans[i][0], ans[i][1]), end=" ")
    print()