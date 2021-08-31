arr = list(map(int, input()))
A = arr.count(0)
B = arr.count(1)
# 0을 뒤집을 때의 카운트
cnt0 = 0
# 1을 뒤집을 때의 카운트
cnt1 = 0
check0 = 0
check1 = 0
for i in range(len(arr)):
    if arr[i] == 0 and check0 == 0:
        check0 = 1
        cnt0 += 1
    elif arr[i] == 1 and check0 == 1:
        check0 = 0
    if arr[i] == 1 and check1 == 0:
        check1 = 1
        cnt1 += 1
    elif arr[i] == 0 and check1 == 1:
        check1 = 0
print(min(cnt0, cnt1))