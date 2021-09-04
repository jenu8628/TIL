def com(idx, sidx, N, R, arr, sel):
    global menu
    if sidx == R:
        temp = ""
        for i in sel:
            temp += i
        if temp not in menu:
            menu[temp] = 1
        else:
            menu[temp] += 1
        return
    # 해당자리를 뽑고 가고
    for i in range(idx, N):
        sel[sidx] = arr[i]
        com(i+1, sidx+1, N, R, arr, sel)


def solution(orders, course):
    answer = []
    global menu
    menu = {}
    for i in course:
        for j in orders:
            if len(j) < i:
                continue
            sel = [0] * i
            com(0, 0, len(j), i, sorted(j), sel)
        if len(menu) != 0 and max(menu.values()) != 1:
            for key, val in menu.items():
                if val == max(menu.values()):
                    answer.append(key)
        menu = {}
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
#
print(solution(orders, course))


# from itertools import combinations
# from collections import Counter
#
#
# def solution(orders, course):
#     answer = []
#     for c in course:
#         temp = []
#         for order in orders:
#             # 조합
#             combi = combinations(sorted(order), c)
#             # 조합 한 것을 리스트에 저장
#             temp += combi
#         # 중복개수 세기
#         counter = Counter(temp)
#         if len(counter) != 0 and max(counter.values()) != 1:
#             answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
#
#     return sorted(answer)
#
# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
#
# course = [2, 3, 4]
#
# print(solution(orders, course))