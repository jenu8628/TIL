# 하영이 풀이

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


# 쌤풀이
priority = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

for tc in range(1, 11):
    input()
    line = input()
    ans = ''
    # 스택 준비
    stack = []

    for i in range(len(line)):
        # 괄호라면
        if line[i] == '(' or line[i] == ')':
            # 여는 괄호는 우선순위가 제일 높으므로 무조건 삽입
            if line[i] == '(':
                stack.append(line[i])
            else:
                # 여는 괄호가 나올 때까지 무조건 pop
                while stack[-1] != '(':
                    ans += stack.pop()
                # 여는 괄호하나 버리기
                stack.pop()
        elif line[i].isdigit():
            ans += line[i]
        # 연산자일 때
        else:
            if len(stack) == 0:
                stack.append(line[i])
            else:
                # 연산자 우선순위를 비교해서
                # 스택에 탑에 있는 연산자가 현재 토큰의 우선순위보다 높거나 같다면
                while priority[stack[-1]] >= priority[line[i]]:
                    ans += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(line[i])
    # 남아있는 스택 비우기
    while len(stack) > 0:
        ans += stack.pop()
# ######################## 중위 표현식 -> 후위표현식
    for i in ans:
        # 숫자면 스택에 쌓기
        if i.isdigit():
            stack.append(int(i))
        # 연산자이면 꺼내서 연산 후 다시 삽입
        else:
            B = stack.pop()
            A = stack.pop()
            if i == '+':
                stack.append(A+B)
            elif i == '-':
                stack.append(A-B)
            elif i == '*':
                stack.append(A*B)
            elif i == '/':
                stack.append(A/B)
    print('#{} {}'.format(tc, stack.pop()))