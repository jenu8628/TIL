def solution(schedule):
    answer = -1
    # schedule은 1,2,3,4,5과목으로 되어있고 A,B,C,D의 네개분반으로 나누어진다.
    # 조합을 하자! schecule의 1번 A분만이면 나머지 조합을 짜는식으로!
    sel = [0] * 5
    M_schedule = [[] for _ in range(5)]
    for i in range(len(schedule)):
        for j in range(len(schedule[i])):
            if len(schedule[i][j]) == 17:
                a, b, c, d = schedule[i][j].split(' ')
                b = int(b[:2]) * 60 + int(b[3:])
                d = int(d[:2]) * 60 + int(d[3:])
                M_schedule[i].append([a, b, c, d])
            else:
                a, b = schedule[i][j].split(' ')
                b = int(b[:2]) * 60 + int(b[3:])
                M_schedule[i].append([a, b])

    return M_schedule
print(len("MO 12:00 WE 14:30"))
schedule = [["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]
print(solution(schedule))