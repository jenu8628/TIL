def backtrack(k):
    global ans
    num = int(''.join(map(str, arr)))
    if num in visit[k]:
        return
    visit[k].add(num)
    if k == int(M):
        if ans < num:
            ans = num
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                arr[i], arr[j] = arr[j], arr[i]
                backtrack(k + 1)
                arr[i], arr[j] = arr[j], arr[i]

for tc in range(1, int(input()) + 1):
    money, M = map(str, input().split())
    ans = 0
    visit = [set() for _ in range(int(M)+1)]
    arr = list(map(int, money))
    N = len(arr)
    backtrack(0)
    print('#{} {}'.format(tc, ans))

