def solution(n, t, m, timetable):
    answer = ''
    tables = []
    # 크루 도착시간 (시 * 60) + 분으로 담기
    for i in timetable:
        a, b = i.split(':')
        tables.append(int(a) * 60 + int(b))
    tables.sort()

    bus = ["540"]
    peoples = {"540": []}
    for i in range(n - 1):
        a = int(bus[i]) + t
        bus.append(str(a))
        peoples[str(a)] = []
    cnt = 0

    for i in range(len(bus)):
        for j in range(cnt, len(tables) + 1):
            if j >= len(tables):
                continue
            if len(peoples[bus[i]]) >= m:
                break
            if tables[j] <= int(bus[i]):
                peoples[bus[i]] += [tables[j]]
                cnt = j+1

    if len(peoples[bus[-1]]) < m:
        a = str(int(bus[-1]) // 60)
        b = str(int(bus[-1]) % 60)
        if len(a) < 2:
            a = "0" + a
        if len(b) < 2:
            b = "0" + b
        answer += '{}:{}'.format(a, b)
    else:
        x = max(peoples[bus[-1]]) - 1
        a = str(x // 60)
        b = str(str(x % 60))
        if len(a) < 2:
            a = "0" + a
        if len(b) < 2:
            b = "0" + b
        answer += '{}:{}'.format(a, b)
    return answer

# n : 셔틀 운행 횟수, t: 셔틀 운행 간격
# m : 한 셔틀에 탈 수 있는 최대 크루 수
# timetable : 크루가 대기열에 도착하는 시각
n, t, m = 1, 1, 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(n, t, m, timetable))


# 버스 운행시간 [시, 분]으로 담기
    # bus = [[9, 0]]
    # for i in range(n-1):
    #     a, b = bus[i][0], bus[i][1] + t
    #     if b == 60:
    #         a, b = a+1, 0
    #     bus.append([a, b])
    # bus.sort(key=lambda x: (-x[0], -x[1]))


# a, b = 9, 0
#     for i in range(n-1):
#         a, b = a, b + t
#         if b >= 60:
#             a, b = a+1, b - 60

# 크루 도착시간 [시, 분]으로 담기
    # for i in timetable:
    #     a, b = i.split(':')
    #     tables.append([int(a), int(b)])
    # tables.sort(key=lambda x: (-x[0], -x[1]))