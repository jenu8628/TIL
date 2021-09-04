import math

def SET(str):
    s = []
    for i in range(len(str) - 1):
        if 65 <= ord(str[i]) <= 90:
            x = str[i]
        elif 97 <= ord(str[i]) <= 122:
            x = chr(ord(str[i]) - 32)
        else:
            continue
        if 65 <= ord(str[i + 1]) <= 90:
            y = str[i + 1]
        elif 97 <= ord(str[i + 1]) <= 122:
            y = chr(ord(str[i + 1]) - 32)
        else:
            continue
        s.append(x + y)
    return s

def solution(str1, str2):
    A = SET(str1)
    B = SET(str2)
    a1 = A[:]
    union = A[:]
    for i in B:
        if i not in a1:
            union.append(i)
        else:
            a1.remove(i)
    # AUB = n(A) + n(B) - n(AnB)
    intersection = len(A) + len(B) - len(union)
    if union == 0 and intersection == 0:
        return 65536
    return math.floor((intersection / len(union)) * 65536)

str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2))

# ord('A') = 65, ord('a') = 97

# def solution(str1, str2):
#     A = SET(str1)
#     B = SET(str2)
#     union = list(set(A) | set(B))
#     intersection = list(set(A) & set(B))
#     if len(union) == 0 and len(intersection) == 0:
#         return 65536
#     return math.floor((len(intersection) / len(union)) * 65536)