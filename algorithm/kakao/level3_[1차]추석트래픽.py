def solution(lines):
    logs = []
    answer = 0
    for line in lines:
        date, time, take = line.split()
        time = time.split(':')
        take = take.replace('s', "")
        # 끝난시간을 밀리초로 환산! 계산하기 편하도록!
        end = (int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])) * 1000
        start = end - (float(take) * 1000) + 1  # 시작시간 포함 이므로
        logs.append([start, end])

    for log in logs:
        # 초당 최대처리량 구하기
        # 1: answer, 2: 로그 시작시간 + 1000(1초), 3: 로그 끝나는시간 + 1000(1초)
        # 무작정 정하는 시간보다 시작시간이나 끝시간을 맞추면 무조건 1개가 포함되므로!
        answer = max(answer, cal(logs, log[0], log[0] + 999), cal(logs, log[1], log[1]+999))
    return answer

# 초당 몇개의 로그를 할 수 있는지 구하는 함수
def cal(logs, start, end):
    count = 0
    for log in logs:
        if log[0] <= end and log[1] >= start:
            count += 1
    return count

lines = [
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]
print(solution(lines))



