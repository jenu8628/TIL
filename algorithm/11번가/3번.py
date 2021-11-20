def solution(N):
    answer = ''
    for i in sorted(str(N), reverse=True):
        answer += i
    if int(answer) > 100000000:
        return -1
    return int(answer)

print(solution(24434))