for tc in range(1, int(input())+1):
    N = int(input())
    arr = []
    for i in range(N):
        st, ed = map(int, input().split())
        arr.append((st, ed))
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j], arr[i]
    cnt = 1
    min_num = arr[0][1]
    for i in range(1, N):
        if arr[i][0] >= min_num:
            min_num = arr[i][1]
            cnt += 1
    print('#{} {}'.format(tc, cnt))