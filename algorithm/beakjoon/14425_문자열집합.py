N, M = map(int, input().split())
arr = {}
ans = 0
for _ in range(N):
    arr[input()] = True
for _ in range(M):
    check = input()
    if arr.get(check):
        ans += 1
print(ans)
