N = int(input())
ans = 99999999
flag = False
for i in range(N):
    num = i
    temp = 0
    for j in str(i):
        temp += int(j)
    num += temp
    if num == N and num < ans:
        ans = i
        flag = True
        break

if flag:
    print(ans)
else:
    print(0)
