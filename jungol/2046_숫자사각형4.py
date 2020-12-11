while True:
    n, m = map(int, input().split())
    if m == 1:
        for i in range(1, n+1):
            for j in range(n):
                print(i, end=" ")
            print()
    elif m == 2:
        for i in range(n):
            for j in range(1, n+1):
                if i % 2 == 0:
                    print(j, end=" ")
                else:
                    print(n-j+1, end=" ")
            print()
    else:
        for i in range(1, n+1):
            for j in range(1, n+1):
                print(i*j, end=" ")
            print()
