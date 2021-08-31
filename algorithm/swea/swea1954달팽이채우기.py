T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    cnt =1
    row_start = 0
    row_end = N-1
    col_start = 0
    col_end = N-1

    while row_start <= row_end and col_start <= col_end:
        #왼쪽 => 오른쪽
        for i in range(col_start, col_end+1):
            arr[row_start][i] = cnt
            cnt += 1
        row_start += 1

        #위 => 아래
        for i in range(row_start, row_end+1):
            arr[i][col_end] = cnt
            cnt += 1
        col_end -= 1

        #오른쪽 => 왼쪽
        for i in range(col_end, col_start-1,-1):
            arr[row_end][i] = cnt
            cnt += 1
        row_end -= 1

        #아래 => 위
        for i in range(row_end, row_start -1, -1):
            arr[i][col_start] = cnt
            cnt += 1
        col_start += 1
    #출력
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()


#쌤풀이
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    d = 0  # 방향 0:우, 1:하, 2:좌, 3:상
    r = 0
    c = 0
    num = 1

    while num <= N * N:
        arr[r][c] = num  # 현재칸에 값을 저장
        num += 1  # 다음숫자준비

        # 다음칸을 결정
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            # 현재좌표를 갱신
            r, c = nr, nc
        else:
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]

    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()