area = ["S", 'D', 'T']


def solution(dartResult):
    # 점수 집계할 리스트
    sco = []
    temp = 0
    for i in range(len(dartResult)):
        if dartResult[i] in area:
            temp = temp ** (area.index(dartResult[i]) + 1)
            sco.append(temp)
            temp = 0
        elif dartResult[i] == '*':
            if len(sco) >= 2:
                sco[-1] = sco[-1] * 2
                sco[-2] = sco[-2] * 2
            else:
                sco[-1] = sco[-1] * 2
        elif dartResult[i] == '#':
            sco[-1] = -sco[-1]
        else:
            if i < len(dartResult) - 1 and 48 <= ord(dartResult[i+1]) <= 57:
                temp += int(dartResult[i]+dartResult[i+1])
            else:
                temp += int(dartResult[i])
    return sum(sco)

dartResult = input()
print(solution(dartResult))