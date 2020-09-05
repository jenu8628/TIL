T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    total = []
    w_cnt = 0
    for w in range(N-2):
        for i in range(M):
            if arr[w][i] != 'W':
                w_cnt += 1
        b_cnt = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if arr[b][j] != "B":
                    b_cnt += 1
            r_cnt = 0
            for r in range(b+1,N):
                for k in range(M):
                    if arr[r][k] != 'R':
                        r_cnt += 1
            total.append(w_cnt + b_cnt + r_cnt)
    print('#{} {}'.format(tc, min(total)))
