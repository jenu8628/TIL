for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    st = 1
    bt = arr[st]
    cnt = 0
    while st + bt < N:
        cnt += 1
        max_bt = 0
        for i in range(st+1, st+bt+1):
            if max_bt < arr[i]+i:
                max_bt = arr[i]+i
                x = i
        st = x
        bt = arr[x]
    print('#{} {}'.format(tc, cnt))