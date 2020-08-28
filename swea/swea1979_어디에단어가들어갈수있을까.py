T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = []
    for i in range(N):
        r_cnt = 0
        c_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                r_cnt += 1
            if arr[i][j] == 0 or j == N-1:
                total.append(r_cnt)
                r_cnt = 0
        for k in range(N):
            if arr[k][i] == 1:
                c_cnt += 1
            if arr[k][i] == 0 or k == N-1:
                total.append(c_cnt)
                c_cnt = 0
    x = total.count(K)
    print('#{} {}'.format(tc, x))
