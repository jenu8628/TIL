arr = [[0]*102 for _ in range(102)]
for i in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(a, c):
        for k in range(b, d):
            arr[j][k] = 1
cnt = 0
for i in range(len(arr)):
    cnt += arr[i].count(1)
print(cnt)