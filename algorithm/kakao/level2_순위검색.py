import pprint
from itertools import combinations
from bisect import bisect_left


def all_cases(temp):
    cases = []
    for k in range(5):
        for comb in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in comb:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = all_cases(i.split())
        print(cases)
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))
    for key in all_people.keys():
        all_people[key].sort()
    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)
    return answer


from collections import defaultdict

def solution2(info, query):
    answer = []
    query = list(map(lambda x: x.replace('and ', '').split(), query))
    applicant = defaultdict(list)
    for resume in info:
        language, stack, career, food, score = resume.split()
        for a in (language, '-'):
            for b in (stack, '-'):
                for c in (career, '-'):
                    for d in (food, '-'):
                        applicant[a+b+c+d].append(int(score))
    # for key in applicant:
    #     applicant[key].sort()
    applicant = dict(map(lambda items: (items[0], sorted(items[1])), applicant.items()))

    for idx, condition in enumerate(query):
        language, stack, career, food, score = condition
        key = language + stack + career + food

        if key not in applicant:
            answer.append(0)
            continue
        start = 0
        end = len(applicant[key])
        mid = 0
        while start < end:
            mid = (start + end) // 2
            if applicant[key][mid] >= int(score):
                end = mid
            else:
                start = mid + 1
        # 0, 10, 0
        # 0, 10, 5
        # 0, 5
        answer.append(len(applicant[key]) - start)
    return answer

from itertools import combinations
from collections import defaultdict
import bisect

def add_all_case(applicant, resume):
    for k in range(5):
        for comb in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in comb:
                    case += resume[idx]
                else:
                    case += '-'
            applicant[case].append(int(resume[4]))
    return applicant

def solution3(info, query):
    answer = []
    query = list(map(lambda x: x.replace('and ', '').split(), query))
    applicant = defaultdict(list)
    for resume in info:
        resume = resume.split()
        add_all_case(applicant, resume)
    applicant = dict(map(lambda items: (items[0], sorted(items[1])), applicant.items()))

    for idx, condition in enumerate(query):
        target = ''.join(condition[0:4])
        score = condition[4]

        if target not in applicant:
            answer.append(0)
            continue
        index = len(applicant[target]) - bisect.bisect_left(applicant[target], int(score))
        answer.append(index)
    return answer


if __name__ == '__main__':
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    # print(solution(info, query))
    # print(solution2(info, query))
    print(solution3(info, query))




# 정확성은 통과한 내 풀이
# def solution(info, query):
#     answer = []
#     # 지원자
#     # 언어, 직군, 경력, 소울푸드, 점수
#     applicant = []
#     for i in info:
#         applicant.append(i.split(" "))
#     applicant.sort(key=lambda x : -int(x[-1]))
#     for i in query:
#         x = i.replace(" and", "").split(" ")
#         temp = 0
#         for j in range(len(applicant)):
#             cnt = 0
#             if int(applicant[j][-1]) < int(x[-1]):
#                 break
#             for k in x:
#                 if k == '-':
#                     cnt += 1
#                 elif k in applicant[j]:
#                     cnt += 1
#                 elif k == x[-1]:
#                     cnt += 1
#             if cnt == 5:
#                 temp += 1
#         answer.append(temp)N
#     return answer
# info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(info, query))

