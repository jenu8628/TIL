def fact(n):
    if 1 >= n:
        return 1
    return n * fact(n-1)


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(fact(i)//(fact(j)*fact(i-j)), end= ' ')
        print()
    
    
    
    #ncp = fact(n)/(fact(p)*fact(n-p))
