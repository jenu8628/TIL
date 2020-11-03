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
    num = 0
    for i in range(len(arr2)):
        cnt = 1
        for j in range(len(arr2[i])):
            if lis[j][arr2[i][j]] == 0:
                cnt = 1
                break
            cnt = cnt * (lis[j][arr2[i][j]] / 100)
        if num < cnt * 100:
            num = cnt * 100
    print('#{} {:.6f}'.format(tc, num))

# 쌤풀이
def DFS(flag, idx, value):
    global ans
    if flag == (1 << N) - 1:
        if ans < value * 100:
            ans = value * 100
        return
    if value * 100 <= ans:
        return
    for i in range(N):
        # 해당 일은 이미 배정되어서 처리함.
        if flag & (1 << i): continue

        DFS(flag | 1 << i, idx+1, value*(work[idx][i] / 100))

for tc in range(1, int(input()) + 1):
    N = int(input())
    work = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    DFS(0, 0, 1)
    print('#{} {:.6f}'.format(tc, ans))