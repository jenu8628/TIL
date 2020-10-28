def baby(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr.count(arr[i]) == 3:
            return 1
    cnt = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        if arr[i] + 1 == arr[i+1]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            return 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    first = []
    second = []
    for i in range(len(arr)):
        if i % 2 == 0:
            first.append(arr[i])
        else:
            second.append(arr[i])
    a = 0
    b = 0
    for i in range(3, len(first)+1):
        a = baby(first[0:i])
        b = baby(second[0:i])
        if a or b:
            break
    if a:
        print('#{} 1'.format(tc))
    elif b:
        print('#{} 2'.format(tc))
    else:
        print('#{} 0'.format(tc))
