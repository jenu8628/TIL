def perm(idx):
    if idx == N:
        tmp = arr[:]
        arr2.append(tmp)
        return
    for i in range(idx, N):
        arr[i], arr[idx] = arr[idx], arr[i]
        perm(idx + 1)
        arr[i], arr[idx] = arr[idx], arr[i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lis = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    for i in range(N):
        arr.append(i)
    arr2 = []
    perm(0)
    ans = []
    for i in range(len(arr2)):
        cnt = 1
        for j in range(len(arr2[i])):
            if lis[j][arr2[i][j]] == 0:
                cnt = 0
                break
            cnt = cnt * (lis[j][arr2[i][j]] / 100)
        ans.append(cnt * 100)
    number = round(max(ans), 6)
    print('#{} {}'.format(tc, number))