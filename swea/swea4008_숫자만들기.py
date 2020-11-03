cal = ['+', '-', '*', '/']
def perm(idx):
    if idx == len(tmp):
        if tmp not in ans:
            arr2 = tmp[:]
            ans.append(arr2)
        return
    for i in range(idx, len(tmp)):
        tmp[i], tmp[idx] = tmp[idx], tmp[i]
        perm(idx+1)
        tmp[i], tmp[idx] = tmp[idx], tmp[i]

def calculate(ans, arr):
    stack = []
    for i in range(len(ans)):
        if not stack:
            x = arr.pop()
            y = arr.pop()
        else:
            x = stack.pop()
            y = arr.pop()
        if ans[i] == '+':
            stack.append(x+y)
        elif ans[i] == '-':
            stack.append(x-y)
        elif ans[i] == '*':
            stack.append(x*y)
        else:
            stack.append(x//y)
    number.extend(stack)
    return

for tc in range(1, int(input()) + 1):
    N = int(input())
    cal_arr = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    tmp = []
    cnt = 0
    for i in range(len(cal_arr)):
        for j in range(cal_arr[i]):
            tmp.append(cal[i])
            if cal[i] == '+' or cal[i] == '-':
                cnt += 1
    if cnt > len(tmp) - cnt:
        r = len(tmp) - cnt
    elif cnt < len(tmp) - cnt:
        r = cnt
    ans = []
    perm(0)
    number =[]
    for i in range(len(ans)):
        lis = arr[::-1]
        calculate(ans[i], lis)
    print('#{} {}'.format(tc, max(number) - min(number)))


# 2번째 풀이
def calculate(ans, arr):
    stack = []
    for i in range(len(ans)):
        if not stack:
            x = arr.pop()
            y = arr.pop()
        else:
            x = stack.pop()
            y = arr.pop()
        if ans[i] == '+':
            stack.append(x+y)
        elif ans[i] == '-':
            stack.append(x-y)
        elif ans[i] == '*':
            stack.append(x*y)
        else:
            stack.append(x//y)
    number.extend(stack)
    return

def comb(idx,sidx, r):
    if sidx == r:
        tmp = sel[:]
        ans.append(tmp)
        return

    if idx == N:
        return

    sel[sidx] = arr[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)

for tc in range(1, int(input()) + 1):
    N = int(input())
    cal_arr = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    tmp = []
    cnt = 0
    ans = []
    for i in range(len(cal_arr)):
        for j in range(cal_arr[i]):
            tmp.append(cal[i])
            if cal[i] == '+' or cal[i] == '-':
                cnt += 1
    if cnt > len(tmp) - cnt:
        # cnt + 1, len(tmp) - cnt
        r = len(tmp) - cnt
        sel = [0] * (len(tmp) - cnt)
        comb(0, 0, r)
    elif cnt < len(tmp) - cnt:
        # len(tmp) - cnt + 1, cnt
        r = cnt
        sel = [0] * cnt
        comb(0, 0, r)
