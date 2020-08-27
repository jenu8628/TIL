T = int(input())
for test_case in range(1, T + 1):
    N = list(map(int,input().split()))
    number = list(map(int,input().split()))
    result = []
    for i in range(0,N[0]-N[1]+1):
        cnt = 0
        for j in range(i, i+N[1]):
            cnt += number[j]
        result.extend([cnt])
    Max = max(result)
    Min = min(result)
    print(f'#{test_case} {Max - Min}')