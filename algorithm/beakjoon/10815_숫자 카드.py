N = int(input())
arr = list(map(int, input().split()))
M = int(input())
check = list(map(int, input().split()))

arr_dict = {i: True for i in arr}

ans = []
#
for i in check:
    if arr_dict.get(i):
        ans.append(1)
    else:
        ans.append(0)

for i, x in enumerate(ans):
    if i == len(ans) - 1:
        print(x)
    else:
        print(x, end=" ")
