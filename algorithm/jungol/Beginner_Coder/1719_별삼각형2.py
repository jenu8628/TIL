while True:
    n, m = map(int, input().split())
    if (0 < n <= 100 and n % 2 == 1) and 1 <= m <= 4:
        if m == 1:
            for i in range(1, n+1):
                if i > (n+1)//2:
                    print('*' * ((n+1)-i))
                else:
                    print('*'*i)
        elif m == 2:
            for i in range(1, n+1):
                if i > (n+1)//2:
                    print(' '*((n+1)//2-((n+1)-i)), end="")
                    print('*' * ((n+1)-i))
                else:
                    print(' ' * ((n + 1)//2 - i), end="")
                    print('*' * i)


    else:
        print("INPUT ERROR!")