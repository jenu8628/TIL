T = int(input())
for test_case in range(1,T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    cnt = 0
    start = 0
    while True:
        if start >= N-K:
            start = start + K
            break
        elif start + K in charge:
            cnt += 1
            start += K
        elif not start + K in charge:
            i_list = []
            for i in range(start+1, start+K):
                if i in charge:
                    i_list.append(i)
            if i_list == []:
                print(f'#{test_case} 0')
                break
            start = max(i_list)
            cnt += 1
    if start >= N:
        print(f'#{test_case} {cnt}')