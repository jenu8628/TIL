import sys
N = int(sys.stdin.readline())
arr1 = []
arr2 = []
arr3 = []
ans = 0
for _ in range(N):
    a = int(sys.stdin.readline())
    if a > 0:
        arr1.append(a)
    elif a == 0:
        arr2.append(a)
    else:
        arr3.append(a)
arr1.sort()
arr3.sort(reverse=True)
while len(arr1) > 0:
    if len(arr1) > 1:
        x = arr1.pop()
        y = arr1.pop()
        if x > 1 and y > 1:
            ans += x * y
        if x == 1 or y == 1:
            ans += x + y
    else:
        ans += arr1.pop()
        break
while len(arr3) > 0:
    if len(arr3) > 1:
        x = arr3.pop()
        y = arr3.pop()
        ans += x * y
    else:
        if len(arr2) > 0:
            pass
        else:
            ans += arr3.pop()
        break
print(ans)