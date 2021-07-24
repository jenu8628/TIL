tc = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 & P == 0 & V == 0:
        break
    else:
        tc += 1
        q = V // P
        r = V % P
        if r > L:
            ans = (L * q) + L
        else:
            ans = (L * q) + r
        print('Case {}: {}'.format(tc, ans))
