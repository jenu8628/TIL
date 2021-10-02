from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    info.reverse()
    combination = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)

    for comb in combination:
        # 라이언이 쏜 과녁
        ryon = [0] * 11

        for i in comb:
            ryon[i] += 1

        # 라이언과 어피치의 점수차이 함수
        num = differnce(info, ryon)
        arr = ryon[::]
        # 점수차이가 기존의 점수차이보다 클때
        if num > 0:
            answer.append([num, arr])

    answer.sort()
    if answer:
        return list(reversed(answer[-1][1]))
    else:
        return [-1]

# 라이언과 어피치의 점수 계산
def differnce(apeach, arr):
    apeach_score = 0
    ryon_score = 0
    for i in range(11):
        if apeach[i] >= arr[i] and apeach[i] != 0:
            apeach_score += i
        elif apeach[i] < arr[i] and arr[i] != 0:
            ryon_score += i
    return ryon_score - apeach_score



# n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
# n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
# n, info = 10, [0,0,0,0,0,0,0,0,3,4,3]
print(solution(n, info))

# 어피치 먼저 n발쏘고 라이언이 n발쏘는 순서
# 만약 k점을 어피치가 a발 맞췄고 라이언이 b발을 맞췄을 경우
# 더 많은 화살을 k점에 맞힌 선수가 k점을 가저감
# 단 a=b일 경우 어피치가 k점을 가져감
# a = b= 0인 경우 라이언과 어피치 모두 점수못가져감
# 최종점수가 높은 사람이 이김
# 최종점수가 같을 경우 어피치가 우승
# 라이언이 가장 큰 점수 차이로 이기기 위해
# n발의 화살을 어떤 과녁 점수에 맞혀야 하는지를 구해라
# 라이언이 우승할 수 없는 경우 [-1]을 리턴


# def solution(n, info):
#     answer = [n+1] * 11
#     score = 0
#     info.reverse()
#     combination = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], n)
#
#     for comb in combination:
#         # 라이언이 쏜 과녁
#         ryon = [0] * 11
#         for i in comb:
#             ryon[i] += 1
#
#         # 라이언과 어피치의 점수차이 함수
#         num = differnce(info, ryon)
#
#         # 점수차이가 기존의 점수차이보다 클때
#         if num >= score and num >= 0:
#             if num > score:
#                 answer = ryon
#             # 같다면!
#             elif num == score:
#                 for i in range(10, -1, -1):
#                     if answer[i] < ryon[i]:
#                         answer = ryon
#                         break
#             score = num
#     if score == 0:
#         return [-1]
#     else:
#         return answer