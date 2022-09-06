area = ["S", 'D', 'T']


def solution1(dartResult):
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


bonus = ['S', 'D', 'T']
def solution2(dartResult):
    answer = []
    score = ''
    for result in dartResult:
        if result.isdigit():
            score += result
        elif result in bonus:
            score = int(score) ** (bonus.index(result) + 1)
            answer.append(score)
            score = ''

        elif result == '*':
            answer[-1] = answer[-1] * 2
            if len(answer) > 1:
                answer[-2] = answer[-2] * 2
        else:
            answer[-1] = -answer[-1]
    return sum(answer)

if __name__ == '__main__':

    # print(solution1('1S2D*3T'))
    # print(solution1('1D2S#10S'))
    # print(solution1('1D2S0T'))
    # print(solution1('1S*2T*3S'))
    # print(solution1('1D#2S*3S'))
    # print(solution1('1T2D3D#'))
    # print(solution1('1D2S3T*'))

    print(solution2('1S2D*3T'))
    print(solution2('1D2S#10S'))
    print(solution2('1D2S0T'))
    print(solution2('1S*2T*3S'))
    print(solution2('1D#2S*3S'))
    print(solution2('1T2D3D#'))
    print(solution2('1D2S3T*'))