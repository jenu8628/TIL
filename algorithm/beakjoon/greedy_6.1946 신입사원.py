import sys
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    arr = []
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        arr.append([a, b])
    arr.sort(key=lambda x: x[0])
    ans = 1
    x = arr[0][1]
    for i in range(1, N):
        if x > arr[i][1]:
            ans += 1
            x = arr[i][1]
    print(ans)