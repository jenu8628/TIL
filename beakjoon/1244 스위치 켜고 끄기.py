K = int(input())
arr = [0] + list(map(int, input().split()))
N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    if a == 1:
        for j in range(1, K+1):
            if j % b == 0:
                arr[j] = (arr[j] + 1) % 2
    elif a == 2:
        arr[b] = (arr[b] + 1) % 2
        for j in range(1, K+1-b):
            if b-j < 1:
                break
            elif arr[b+j] == arr[b-j]:
                arr[b+j] = (arr[b+j] + 1) % 2
                arr[b-j] = (arr[b-j] + 1) % 2
            if arr[b+j] != arr[b-j]:
                break
for i in range(1, K+1):
    print(arr[i], end=" ")
    if i % 20 == 0:
        print()