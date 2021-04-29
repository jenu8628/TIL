while True:
    N, K = map(int, input().split())
    ans = 0
    cnt = 0
    for i in range(1, N+1):
        # i 가 N의 약수이면
        if N % i == 0:
            # 카운트를 센다
            cnt += 1
            # 카운트가 K이면
            if cnt == K:
                # i가 정답!
                ans = i
                break
    print(ans)