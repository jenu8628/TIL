from collections import deque

def solution(P):
    ans = []
    temp = []
    for i in range(1, len(P)):
        right = P[0] + P[i]
        left = P[i] + P[0]
        if right == right[::-1]:
            temp.append(P[i])
        elif left == left[::-1]:
            temp.append(P[i])

    for i in range(len(temp)):
        Q = deque(P)
        a = temp[i]
        while True:
            x = Q.popleft()
            y = Q.popleft()
            if y == a:
                break
            Q.appendleft(x)
            Q.append(y)
        check = True
        flag = False
        while Q:
            if flag and len(Q) == 0:
                break
            x = Q.popleft()
            for j in range(len(Q)):
                y = Q.popleft()
                right = x + y
                left = y + x
                if right == right[::-1]:
                    flag = True
                    break
                elif left == left[::-1]:
                    flag = True
                    break
                Q.append(y)
            if not flag:
                check = False
                break
        if check:
            ans.append(a)
    return ans

print(solution(["11","111","11","211"]))
print(solution(["21","123","111","11"]))
# 111 111
# a = '12345'
# print(a[3:][::-1])
