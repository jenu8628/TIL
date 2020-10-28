T = int(input())
for tc in range(1, T+1):
    N = float(input())
    i = 1
    ans = ''
    while N > 0:
        if 2**(-i) <= N:
            N = N - 2**(-i)
            ans += '1'
        else:
            ans += '0'
        i += 1
        if len(ans) > 12:
            print('#{} overflow'.format(tc))
            break
    if len(ans) <= 12:
        print('#{} {}'.format(tc, ans))