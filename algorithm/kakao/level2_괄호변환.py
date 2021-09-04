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
    # 반복문
    # for i in range(len(string)):
    #     if string[i] == '(':
    #         left += 1
    #     else:
    #         right += 1
    #     if left == right:
    #         u += string[0:i+1]
    #         v += string[i+1:]
    #         break

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

def solution(p):
    return p if is_correct(p) else recursive(p)
