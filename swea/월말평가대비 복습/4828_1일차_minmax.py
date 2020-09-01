T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_number = arr[0]
    max_number = arr[0]
    for i in range(N):
        if min_number > arr[i]:
            min_number = arr[i]
        if max_number < arr[i]:
            max_number = arr[i]
    print("#{} {}".format(tc, max_number - min_number))