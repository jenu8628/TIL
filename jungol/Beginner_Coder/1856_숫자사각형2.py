while True:
    n, m = map(int, input().split())
    idx = 1
    d = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            for j in range(m*i-m+1, m*i+1):
                print(j, end=" ")
        else:
            for j in range(m*i, m*i-m, -1):
                print(j, end=" ")
        print()