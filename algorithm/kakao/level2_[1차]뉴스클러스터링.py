import math
from collections import defaultdict


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


def solution2(str1, str2):
    str_set = set()
    str1_dict = make_string_set(str1, str_set)
    str2_dict = make_string_set(str2, str_set)
    intersection_cnt = 0    # 교집합
    union_cnt = 0           # 합집합

    for string in str_set:
        max_cnt = max(str1_dict[string], str2_dict[string])
        min_cnt = min(str1_dict[string], str2_dict[string])
        if min_cnt != 0:
            intersection_cnt += min_cnt
        union_cnt += max_cnt
    if intersection_cnt == union_cnt == 0:
        return 65536
    return math.floor((intersection_cnt/union_cnt) * 65536)

def is_str(string):
    if 65 <= ord(string) <= 90:
        return chr(ord(string) + 32)
    elif 97 <= ord(string) <= 122:
        return string
    return ""

def make_string_set(string, str_set):
    result = defaultdict(int)
    # result = []
    for idx in range(len(string) - 1):
        left = is_str(string[idx])
        right = is_str(string[idx + 1])
        if len(left + right) == 2:
            result[left + right] += 1
            str_set.add(left+right)
    return result


if __name__ == '__main__':
    # print(solution("FRANCE", "french"))
    # print(solution("handshake", "shake hands"))
    # print(solution("aa1+aa2", "AAAA12"))
    # print(solution("E=M*C^2", "e=m*c^2"))
    print(solution2("FRANCE", "french"))
    print(solution2("handshake", "shake hands"))
    print(solution2("aa1+aa2", "AAAA12"))
    print(solution2("E=M*C^2", "e=m*c^2"))
