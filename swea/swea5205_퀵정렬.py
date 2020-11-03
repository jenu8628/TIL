def quik(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quik(arr, l, s-1)
        quik(arr, s+1, r)

def partition(arr, l, r):
    p = arr[l]
    i = l
    j = r
    while i <= j:
        while i < len(arr) and arr[i] <= p:
            i += 1
        while j > 0 and arr[j] >= p:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quik(arr, 0, len(arr)-1)
    print(arr)
    print('#{} {}'.format(tc, arr[N//2]))