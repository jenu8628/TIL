n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
from itertools import combinations_with_replacement
def solution(n, info):
    answer = []
    info.reverse()

    combi = list(combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n))

    save = []
    for c in combi:
        lion = [0]*11
        peach = 0
        for i in c:
            lion[i] += 1

        tmp = lion[::]
        s = score(info, tmp)
        if s> 0:
            save.append([s, tmp])

    save.sort()

    if save:
        answer = list(reversed(save[-1][1]))
    else:
        answer = [-1]
    return answer

def score(info, tmp):
    ap, li = 0, 0


    for i in range(0, 11):
        if info[i] >= tmp[i] and info[i] != 0:
            ap += i
        elif tmp[i] > info[i] and tmp[i] !=0:
            li += i

    return li-ap


print(solution(n, info))