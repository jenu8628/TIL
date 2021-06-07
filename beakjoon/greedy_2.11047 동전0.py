N, K = map(int, input().split())
arr = []
for i in range(N):
    x = int(input())
    if x <= K:
        arr.append(x)
con = K
cnt = 0
i = len(arr)-1
while con > 0:
    if arr[i] <= con:
        a = con // arr[i]
        con -= arr[i] * a
        cnt += a
    elif arr[i] > con:
        i -= 1
print(cnt)