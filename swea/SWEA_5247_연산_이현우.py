for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visit = [0] * 1000001
    Q = [(N, 0)]
    i = 0
    visit[N] = 1
    idx = 0
    while True:
        x = Q[idx]
        idx += 1
        i = x[1] + 1
        if x[0]*2 == M or x[0] + 1 == M or x[0]-10 == M or x[0] - 1 == M:
            break
        if x[0] < M:
            if visit[x[0] * 2] == 0 and x[0] * 2 < 1000001:
                Q.append((x[0] * 2, i))
                visit[x[0] * 2] = 1

            if visit[x[0] + 1] == 0 and x[0] + 1 < 1000001:
                Q.append((x[0] + 1, i))
                visit[x[0] + 1] = 1
        if visit[x[0]-10] == 0 and 0 < x[0]-10:
            Q.append((x[0]-10, i))
            visit[x[0]-10] = 1

        if visit[x[0] - 1] == 0 and 0 < x[0] - 1:
            Q.append((x[0] - 1, i))
            visit[x[0] - 1] = 1
    print('#{} {}'.format(tc, i))