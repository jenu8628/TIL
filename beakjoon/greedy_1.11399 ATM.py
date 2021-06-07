N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0
for i in range(N):
    x = 0
    for j in range(i+1):
        x += arr[j]
    ans += x
print(ans)