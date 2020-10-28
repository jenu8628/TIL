def ternary(arr):
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[-(i+1)] * (3 ** i)
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    two = []
    three = []
    for i in range(len(N)):
        tmp = list(map(int, N))
        tmp[i] = (tmp[i]+1) % 2
        cnt = 0
        for j in range(len(tmp)):
            cnt += tmp[-(j+1)] * (2 ** j)
        two.append(cnt)
    for j in range(1, 3):
        for i in range(len(M)):
            tmp = list(map(int, M))
            tmp[i] = (tmp[i]+j) % 3
            three.append(tmp)
    for i in range(len(three)):
        if ternary(three[i]) in two:
            print('#{} {}'.format(tc, ternary(three[i])))