# 01D06079861D79F99F
# 2진수 변경 함수(순서가 반대)
def binary(x):
    bin = []
    while x:
        bin.append(x % 2)
        x = x // 2
    return bin

arr = list(input())
tmp = ['A', 'B', 'C', 'D', 'E', 'F']
# 16진수 인트형태로 변환
for i in range(len(arr)):
    if arr[i] in tmp:
        arr[i] = tmp.index(arr[i]) + 10
    else:
        arr[i] = int(arr[i])
# 16진수 -> 2진수 / 4비트씩 맞춰서 ans에 추가
ans = []
for i in range(len(arr)):
    lis = binary(arr[i])
    if len(lis) != 4:
        while len(lis) < 4:
            lis.append(0)
    for j in range(len(lis)-1, -1, -1):
        ans.append(lis[j])
# 2진수 -> 10진수
for i in range(0, len(ans), 7):
    answer = ans[i:i+7]
    cnt = 0
    for j in range(1, len(answer)+1):
        if answer[-j] == 1:
            cnt += answer[-j] << j-1
    if i >= len(ans) - 7:
        print(cnt)
    else:
        print(cnt, end=', ')