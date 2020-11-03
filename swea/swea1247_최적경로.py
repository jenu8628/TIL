def perm(idx):
    if idx == len(tmp):
        lis = [0] + [1] + tmp[:]
        ans.append(lis)
        return
    for i in range(idx, len(tmp)):
        tmp[i], tmp[idx] = tmp[idx], tmp[i]
        perm(idx+1)
        tmp[i], tmp[idx] = tmp[idx], tmp[i]


for tc in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr1 = []
    for i in range(0, len(arr), 2):
        arr1.append([arr[i], arr[i+1]])
    tmp = []
    ans = []
    for i in range(2, 2+N):
        tmp.append(i)
    perm(0)

    for i in range(len(ans)):
        num = 0
        for j in range(len(ans[i]))
        x = abs(arr1[ans[i]][0] -arr1[ans[i]][1])

    print(ans)