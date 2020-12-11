while True:
    n, m = map(int, input().split())
    idx = 1
    while idx <= n*m:
        if idx % m == 1 and idx != 1:
            print()
        print(idx, end=" ")
        idx += 1