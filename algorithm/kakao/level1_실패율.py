from collections import defaultdict


def solution(N, stages):
    # 해당 스테이지를 이미 깨서 지나쳤거나 도달한 총인원
    all_p = [0] * N
    # 해당 스테이지에 머물고 있는 인원
    arrive_p = [0] * N
    # (라운드,실패율) 담을 리스트
    basket = []
    for i in stages:
        if i > N:
            for j in range(i-1):
                all_p[j] += 1
        else:
            arrive_p[i-1] += 1
            for j in range(i):
                all_p[j] += 1
    for i in range(N):
        if all_p[i] == 0:
            basket.append((i+1, 0))
        else:
            basket.append((i+1, arrive_p[i] / all_p[i]))
    basket.sort(key=lambda x: (-x[1], x[0]))
    answer = list(zip(*basket))[0]
    # answer = [i[0] for i in basket]
    # for i in basket:
    #     answer.append(i[0])
    return answer


def solution2(N, stages):
    arrive_list = [0] * N
    pass_list = [0] * N
    fail_rate_dict = {}

    for stage in stages:
        if stage > N:
            stage = stage - 1
        else:
            arrive_list[stage - 1] += 1
        for j in range(stage):
            pass_list[j] += 1

    for i in range(N):
        if pass_list[i] == 0:
            fail_rate_dict[i+1] = 0
            continue
        fail_rate_dict[i+1] = arrive_list[i] / pass_list[i]

    fail_rate_dict = sorted(fail_rate_dict.items(), key=lambda x: (-x[1], x[0]))
    return list(list(zip(*fail_rate_dict))[0])


if __name__ == '__main__':
    # print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # print(solution(4, [4,4,4,4,4]))
    print(solution2(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # print(solution2(4, [4, 4, 4, 4, 4]))




# 도달 But Not clear 인원/ 도달한 인원
# 전체 스테이지 개수
# stages : 현재 멈춰있는 스테이지의 번호
# N+1은 마지막까지 클리어한 사용자
# 만약 실패율이 같은 스테이지가 있다? 작은 번호의 스테이지가 먼저 오도록
# 스테이지에 도달 유저 X 해당 스테이지 실패율 = 0
# 실패율이 높은 스테이지 부터 내림차순으로 스테이지 번호가 담겨있는 배열 return
