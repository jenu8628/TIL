# 기호
te = ["*", "-", "+"]

# 순열
def per(idx, N):
    if idx == N:
        arr.append(sign[:])
        return
    for i in range(idx, N):
        sign[idx], sign[i] = sign[i], sign[idx]
        per(idx+1, N)
        sign[idx], sign[i] = sign[i], sign[idx]

    return

def cal(num, arr):
    # arr : 계산 순서
    # num 계산할 리스트
    stack = []
    for i in range(len(arr)):
        if i == 0:
            lis = num[:]
        else:
            lis = stack[:]
            stack = []
        while lis:
            x = lis.pop(0)
            if x == arr[i]:
                a = stack.pop()
                b = lis.pop(0)
                if x == "*":
                    stack.append(a * b)
                elif x == "-":
                    stack.append(a - b)
                else:
                    stack.append(a + b)
            else:
                stack.append(x)
    return abs(stack[0])


def solution(expression):
    global arr
    global sign
    answer = 0
    sign = []
    num = []
    mid = 0
    # 리스트화 및 몇개의 연산기호가 있는지 확인 후 담기
    for i in range(len(expression)):
        if i < mid:
            continue
        for j in range(i+1, len(expression)):
            if expression[j] in te:
                if expression[j] not in sign:
                    sign.append(expression[j])
                num.append(int(expression[i:j]))
                num.append(expression[j])
                mid = j+1
                if mid == len(expression) - 1:
                    num.append(int(expression[mid:]))
                break
            if j == len(expression) - 1:
                num.append(int(expression[i:]))

    arr = []
    per(0, len(sign))
    for i in range(len(arr)):
        if cal(num, arr[i]) > answer:
            answer = cal(num, arr[i])
    return answer


from collections import deque
from itertools import permutations

def solution2(expression):
    temp = ""
    exp_list = []
    math_expression = set()
    for idx, s in enumerate(expression):
        if s == '+' or s == '*' or s == '-':
            exp_list += [temp, s]
            math_expression.add(s)
            temp = ""
            continue
        temp += s
        if idx == len(expression) - 1:
            exp_list.append(temp)
    perm_expression = permutations(math_expression)
    max_num = 0

    for sign_list in perm_expression:
        q = deque(exp_list)
        for idx, sign in enumerate(sign_list):
            temp = []
            while True:
                x, exp, y = q.popleft(), q.popleft(), q.popleft()
                if exp == sign:
                    result = calculate_num(sign, int(x), int(y))
                    if len(q) == 0:
                        temp.append(result)
                        break
                    q.appendleft(result)
                else:
                    if len(q) == 0:
                        temp += [x, exp, y]
                        break
                    temp += [x, exp]
                    q.appendleft(y)
            q = deque(temp)
        if max_num < abs(q[0]):
            max_num = abs(q[0])
    return max_num

def calculate_num(sign, x, y):
    if sign == '+':
        result = x + y
    elif sign == '*':
        result = x * y
    else:
        result = x - y
    return result

from collections import deque
from itertools import permutations

cals = [
    ['+','-','*'],
    ['+','*','-'],
    ['-','+','*'],
    ['-','*','+'],
    ['*','-','+'],
    ['*','+','-'],
]

def solution3(expression):
    max_num = 0
    for cal in cals:
        temp_list = []
        for i in expression.split(cal[0]):
            temp = [f'({j})' for j in i.split(cal[1])]
            temp_list.append(f'({cal[1].join(temp)})')
        result = abs(eval(cal[0].join(temp_list)))
        max_num = result if result > max_num else max_num
    return max_num


if __name__ == '__main__':

    # print(solution("50*6-3*2"))
    # print(solution("100-200*300-500+20"))

    print(solution2("50*6-3*2"))
    print(solution2("100-200*300-500+20"))

    # 음수라면 해당 숫자의 절댓값으로 변환하여 제출!

