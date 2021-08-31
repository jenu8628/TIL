while True:
    n, m = map(int, input().split())
    if 1<= n <= 100 and 1<= m <= 3:
        if m == 1:
            for i in range(1,n+1):
                print('*'* i)
        elif m == 2:
            for i in range(n, 0, -1):
                # print(i)
                print('*'* i)
        else:
            for i in range(n):
                print(" "*(((2*n)-((i*2)+1))//2),end="")
                print("*"*((i*2)+1),end="")
                print(" " * (((2 * n) - ((i * 2) + 1)) // 2))
    else:
        print("INPUT ERROR!")