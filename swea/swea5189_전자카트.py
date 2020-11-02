def perm(idx):
    if idx == N:
        ans.append(sel+[0])
        return
    if sel[0] != 0:
        return
    for i in range(idx, N):
        sel[idx], sel[i] = sel[i], sel[idx]
        perm(idx+1)
        sel[idx], sel[i] = sel[i], sel[idx]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sel = [0] * N
    for i in range(N):
        sel[i] = i
    ans = []
    perm(0)
    min_num = 9999999999999999999999
    for i in range(len(ans)):
        cnt = 0
        for j in range(len(ans[i])-1):
            cnt += arr[ans[i][j]][ans[i][(j+1)]]
            if cnt > min_num:
                break
        if min_num > cnt:
            min_num = cnt
    print('#{} {}'.format(tc, min_num))