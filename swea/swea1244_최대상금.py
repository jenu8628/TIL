for tc in range(1, int(input()) + 1):
    N, M = map(str, input().split())
    arr = list(map(int, N))

    for i in range(int(M)):
        # 최대
        a, c, b = arr[i], i, 0
        while c < N:
            if a < arr[c]:
                a = arr[c]
                b = c
            c += 1
        #최소
        # x, r, y = arr[0], 1, 0
        # while r <= N-b:
        #     if x > arr[r]:
        #         x = arr[r]
        #         y = r
        #     r += 1
        # 만약 arr[i]가 b보다 크면?
        if arr[b]:
            pass
        arr[b], arr[i] = arr[i], arr[b]
        
    # for i in range(len(arr)):
    #     for j in range(len(arr)-1, i,-1):
    #         if arr[j] == max(arr):
    #             arr[i], arr[j] = arr[j], arr[i]
    #             break
    print('#{}'.format(tc), end=' ')
    for i in range(len(arr)):
        print(arr[i], end='')
    print()

