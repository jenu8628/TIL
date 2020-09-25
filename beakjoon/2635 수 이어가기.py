N = int(input())
result = []
for i in range(N, -1, -1):
    arr = [N]
    arr.append(i)
    while True:
        tmp = arr[:]
        b = tmp.pop()
        a = tmp.pop()
        c = a - b
        if c < 0:
            break
        arr.append(c)
    if len(arr) > len(result):
        result = arr[:]
print(len(result))
print(*result)