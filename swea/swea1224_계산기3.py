cal = ['+', '*']
br = ['(', ')']

# 우선순위 *가 1, +가 0
def pf(x):
    if x == '*':
        return 1
    return 0

# 숫자인지 판단
def is_num(x):
    if x not in cal and x not in br:
        return True
    return False

# 중위표기법 -> 후위표기법
def trans(line):
    for l in line:
        # 숫자일 경우
        if is_num(l):
            res.append(l)
        # 기호일 경우 우선순위 따지기
        elif l in cal:
            p = pf(l)
            while len(stack) > 0:
                top = stack[-1]
                if pf(top) <= p:
                    break
                res.append(stack.pop())
            stack.append(l)
        elif l == '(':
            stack.append(l)
        # 괄호 내의 모든 기호 pop
        elif l == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                res.append(x)
    # 기호 남아있을 경우 전부 출력력
    while len(stack) > 0:
        res.append(stack.pop())

# 후위표기법 -> 계산
def calculate(line):
    for l in line:
        # 기호일 경우 앞 두 숫자 pop해서 결과값 다시 stack에 append
        if l in cal:
            y, x = int(stack.pop()), int(stack.pop())
            if l == '+':
                ans = x + y
            else:
                ans = x * y
            stack.append(ans)
        # 숫자일 경우 stack에 저장
        else:
            stack.append(l)

for tc in range(1, 11):
    N = int(input())
    line = input()
    res = []
    stack = []
    trans(line)
    calculate(res)
    print('#{} {}'.format(tc, stack[0]))