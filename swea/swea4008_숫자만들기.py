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
    for i in range(len(cal_arr)):
        for j in range(cal_arr[i]):
            tmp.append(cal[i])
    ans = []
    perm(0)
    number =[]
    for i in range(len(ans)):
        lis = arr[::-1]
        calculate(ans[i], lis)
    print('#{} {}'.format(tc, max(number) - min(number)))