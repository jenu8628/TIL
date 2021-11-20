import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    arr = []
    for _ in range(N):
        arr.append(sys.stdin.readline().rstrip())
    arr.sort()
    ans = "YES"
    for i in range(N-1):
        length = len(arr[i])
        if arr[i] == arr[i+1][:length]:
            ans = "NO"
            break
    print(ans)



