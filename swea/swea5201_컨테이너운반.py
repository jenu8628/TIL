for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    t = sorted(list(map(int, input().split())))
    cnt = 0
    for i in range(len(t)-1, -1, -1):
        max_num = 0
        for j in range(len(w)-1, -1, -1):
            if t[i] >= w[j]:
                cnt += w[j]
                w = w[:j]
                break
    print('#{} {}'.format(tc, cnt))