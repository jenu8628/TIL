while True:
    N, M = map(int, input().split())
    if N < M:
        Common = 1
        for i in range(1,N+1):
            if N % i == 0:
                if M % i == 0:
                    if i > Common:
                        Common = i
    else:
        Common = 1
        for i in range(1, M + 1):
            if M % i == 0:
                if N % i == 0:
                    if i > Common:
                        Common = i
    print(Common)
    print((N * M)//Common)