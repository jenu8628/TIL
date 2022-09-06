from collections import OrderedDict

def solution(waiting):
    # answer = sorted(set(waiting), key=lambda x: waiting.index(x))
    # answer = list(dict.fromkeys(waiting))
    answer = list(OrderedDict.fromkeys(waiting))
    return answer

# 중복없애기
# set을 이용하면 시간초과
# for문이용 시간초과
# dict이용 성공
# dict.fromkeys : 딕셔너리 생성법 첫인자가 딕셔너리 key값이됨
# dict를 다시 list로 하면 키값으로 이루어짐
print(solution([1, 5, 8, 2, 10, 5, 4, 6, 4, 8]))
# print(solution([5, 4, 4, 3, 5]))