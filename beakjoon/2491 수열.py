def p(num):
    global max_num
    cnt = 1
    for i in range(1, N):
        if num[i - 1] <= num[i]:
            cnt += 1
        else:
            cnt = 1
        if max_num < cnt:
            max_num = cnt

N = int(input())
arr = list(map(int, input().split()))
cnt = 1
max_num = 1
p(arr)
p(arr[::-1])
print(max_num)