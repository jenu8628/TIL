while True:
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    idx = 65
    for i in range(n):
        for j in range(n):
            if idx > 90:
                idx = 65
            if i % 2 == 0:
                arr[j][i] = chr(idx)
            else:
                arr[n-j-1][i] = chr(idx)
            idx += 1
    for i in range(n):
        print(*arr[i])