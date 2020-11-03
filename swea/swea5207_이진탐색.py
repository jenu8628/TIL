def bina(arr, l, r, x):
    global cnt
    tmp = -1
    while True:
        mid = (r + l) // 2
        if arr[mid] == x:
            cnt += 1
            return
        elif x < arr[mid]:
            r = mid - 1
            now = 0
        elif arr[mid] < x:
            l = mid + 1
            now = 1
        if tmp == now:
            break
        tmp = now

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    cnt = 0
    for i in range(len(B)):
        if B[i] in A:
            bina(A, 0, len(A)-1, B[i])
    print('#{} {}'.format(tc, cnt))