T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    max_cnt = 0
    min_cnt = 0
    for i in range(N):
        arr = list(map(int, input().split()))
        cnt = 0
        for j in range(M):
            if arr[j] == answer[j]:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
        if cnt < min_cnt:
            min_cnt = cnt

    print('#{} {}'.format(tc, num))