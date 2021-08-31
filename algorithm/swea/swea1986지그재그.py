T = int(input())
for tc in range(1,T+1):

    N = int(input())
    # total에 홀수는 더하고 짝수는 빼기
    total = 0
    for i in range(1, N+1):
        # 홀수라면 total에 더해주기
        if i % 2 == 1:
            total += i
        # 짝수라면 total에 빼주기
        elif i % 2 == 0:
            total -= i

    print('#{} {}'.format(tc, total))