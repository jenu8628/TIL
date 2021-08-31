def f(idx):
    if idx == M:
        for j in sel:
            print(j, end=' ')
        print()
        return

    for i in range(N):
        if not visit[i]:
            sel[idx] = arr[i]
            visit[i] = 1
            f(idx+1)
            visit[i] = 0

N, M = map(int, input().split())
arr = []
sel = [0]*M
visit = [0]*N
for i in range(1, N+1):
    arr.append(i)
f(0)