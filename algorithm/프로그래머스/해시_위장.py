from collections import Counter

def solution(clothes):
    answer = 1
    cnt = Counter([kind for name, kind in clothes])
    ans = []
    for i in cnt.values():
        answer *= (i+1)
    return answer - 1