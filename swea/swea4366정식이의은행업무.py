# 내풀이
def ternary(arr):
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[-(i + 1)] * (3 ** i)
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = list(map(int, input()))
    M = list(map(int, input()))
    two = []
    three = []

    for i in range(len(N)):
        tmp = N[:]
        tmp[i] = (tmp[i] + 1) % 2
        cnt = 0
        for j in range(len(tmp)):
            cnt += tmp[-(j + 1)] * (2 ** j)
        two.append(cnt)

    for j in range(1, 3):
        for i in range(len(M)):
            tmp = M[:]
            tmp[i] = (tmp[i] + j) % 3
            three.append(tmp)
    for k in range(len(three)):
        if ternary(three[k]) in two:
            print('#{} {}'.format(tc, ternary(three[k])))
            break


# 쌤풀이
def check(num, notation):
    change_num = int(num, notation)
    idx = len(num) - 1
    for i in map(int, num):
        for j in range(notation):
            if i == j:
                continue
            tmp = change_num - i * (notation ** idx) + j * (notation ** idx)
            if tmp not in ans:
                ans.append(tmp)
            else:
                return tmp
        idx -= 1
for tc in range(1, int(input()) + 1):
    num2 = input()
    num3 = input()
    # 한 비트씩 바꾼 10진수를 저장할 리스트
    ans = []
    check(num2, 2)
    print('#{} {}'.format(tc, check(num3, 3)))
