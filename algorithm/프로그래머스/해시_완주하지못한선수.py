# def solution(participant, completion):
#     answer = ""
#     user = dict.fromkeys(participant, 0)
#     for i in participant:
#         user[i] += 1
#     for i in completion:
#         user[i] -= 1
#     for i in user:
#         if user[i] != 0:
#             answer += i
#             break
#     return answer


import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]