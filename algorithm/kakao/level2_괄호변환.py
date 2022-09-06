from collections import deque


def is_correct(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return not stack

# u, v로 분리
def detatch(string):
    str_que = deque(string)
    left, right = 0, 0
    u, v = "", ""

    # que사용
    while str_que:
        u += str_que.popleft()
        if u[-1] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    v = "".join(list(str_que))
    return u, v

def reverse(u): #뒤집기
    return ''.join([')' if s == '(' else '(' for s in u])

def recursive(string):
    if string == "":    # 1번
        return ''
    u, v = detatch(string)  # 2번
    if is_correct(u):   # 3번
        return u + recursive(v)
    else:   # 4번
        return '(' + recursive(v) + ')' + reverse(u[1:-1])

def solution1(p):
    return p if is_correct(p) else recursive(p)






def detach_string(string):
    u, v = "", ""
    l_cnt, r_cnt = 0, 0
    # u, v 분리
    for idx, bracket in enumerate(string):
        u += bracket
        if bracket == '(':
            l_cnt += 1
        else:
            r_cnt += 1
        if l_cnt == r_cnt and idx < len(string):
            # u가 균형잡힌 괄호 문자열이 된 경우
            v = string[idx+1:]
            break
    return u, v

def is_correct_string(string):
    # 스택을 사용해서 올바른 괄호 문자열인지 확인한다.
    stack = []

    for s in string:
        if s == '(':
            stack.append(s)
        # s==')' and stack이 비어있지 않을 때가 포함
        # if s == ')' and stack != [] 과 같다.
        elif stack:
            stack.pop()
    # stack안에 (가 남아있다면 false를 반환
    # stack이 비어있다면 올바른 괄호 문자열이므로 true를 반환
    return not stack

def reverse_string(string):
    # string을 돌면서  ( -> )로 ) -> (로 변경한다.
    # 컴프리핸션 기법 사용
    return "".join(')' if s == '(' else '(' for s in string)

def recursive_func(string):
    # 1. 빈 문자열일 경우 빈 문자열 반환
    if not string:
        return ""
    # 2. 균형잡힌 괄호 문자열 u와 나머지 v로 분리
    u, v = detach_string(string)
    # 3. u가 균형잡힌 문자열이라면
    if is_correct_string(u):
        # v는 1단계부터 다시 진행하여 3-1. u에 이어 붙혀서 반환
        return u + recursive_func(v)
    else:
        # 4. 문자열 u가 올바른 괄호 문자열이 아니라면 4의 과정을 수행
        return '(' + recursive_func(v) + ')' + reverse_string(u[1:-1])

def solution2(p):
    # 올바른 괄호 문자열이라면 그대로 반환
    return p if is_correct_string(p) else recursive_func(p)









if __name__ == '__main__':
    # print(solution1("(()())()"))
    # print(solution1(")("))
    # print(solution1("()))((()"))
    print(solution2("(()())()"))
    print(solution2(")("))
    print(solution2("()))((()"))



