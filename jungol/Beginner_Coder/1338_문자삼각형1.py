while True:
    N = int(input())
    arr = [[" "]*N for _ in range(N)]
    k = 65
    for i in range(N):
        j, n = i, N-1
        while j < N:
            arr[j][n] = chr(k)
            k += 1
            j += 1
            n -= 1
            if k == 91:
                k = 65
    for i in range(N):
        print(*arr[i])