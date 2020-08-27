T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    print('#{}'.format(tc), end = ' ')
    for k in range(N):
        print('{}'.format(number[k]), end = ' ')
    print()