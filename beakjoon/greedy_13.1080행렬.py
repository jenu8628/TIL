def check(r, c):
    for i in range(3):
        for j in range(3):
            A[r+i][c+j] = str((int(A[r+i][c+j])+1) % 2)


N, M = map(int, input().split())
A = [list(map(str, input())) for _ in range(N)]
B = [list(map(str, input())) for _ in range(N)]
if N < 3 or M < 3:
    if A != B:
        print(-1)
    else:
        print(0)
else:
    ans = 0
    if A != B:
        for i in range(N - 2):
            for j in range(M - 2):
                if A[i][j] != B[i][j]:
                    ans += 1
                    check(i, j)
                    if A == B:
                        break

    if A != B:
        print(-1)
    else:
        print(ans)
