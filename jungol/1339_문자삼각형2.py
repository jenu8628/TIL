while True:
    N = int(input())
    if N < 1 or N > 100 or N % 2 == 0:
        print("INPUT ERROR")
    else:
        arr = [[" "] * N for _ in range(N)]
        k = 65
        for i in range(N//2, -1, -1):
            for j in range(i, (N // 2) * 2 - i + 1):
                arr[j][i] = chr(k)
                k += 1
                if k == 91:
                    k = 65
        for i in range(N):
            print(*arr[i])