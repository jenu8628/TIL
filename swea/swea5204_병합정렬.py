def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    left = merge_sort(arr[0:m])
    right = merge_sort(arr[m:])
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left[::-1], right[::-1])

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[-1] <= right[-1]:
                result.append(left.pop())
            else:
                result.append(right.pop())
        elif len(left) > 0:
            result.append(left.pop())
        elif len(right) > 0:
            result.append(right.pop())
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))