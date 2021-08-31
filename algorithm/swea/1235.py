str_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
result = ['-', '_', '.']


def solution(new_id):
    answer_1 = ''
    answer_2 = ''
    answer_3 = ''
    answer_4 = ''
    answer_5 = ''
    answer_6 = ''
    answer_7 = ''
    # 1단계
    for i in new_id:
        if ord(i) >= 65 and ord(i) <= 90:
            i = chr(ord(i) + 32)
        answer_1 += i
    # 2단계
    for i in answer_1:
        if i.isdigit() or i in str_s or i in result:
            answer_2 += i
    # 3단계
    for i in range(len(answer_2)):
        if i + 1 < len(answer_2) and answer_2[i] == '.' and answer_2[i + 1] == '.':
            continue
        answer_3 += answer_2[i]
    # 4단계
    for i in range(len(answer_3)):
        if i == 0 and answer_3[i] == '.':
            continue
        if i == len(answer_3) - 1 and answer_3[i] == '.':
            continue
        answer_4 += answer_3[i]
    # 5단계
    if len(answer_4) == 0:
        answer_5 = 'a'
    else:
        answer_5 = answer_4

    # 6단계
    for i in range(len(answer_5)):
        if i == 14 and answer_5[i] == '.':
            continue
        if i >= 15:
            continue
        answer_6 += answer_5[i]
    # 7단계
    if len(answer_6) <= 2:
        answer_7 = answer_6
        while len(answer_7) < 3:
            answer_7 += answer_6[-1]
    else:
        answer_7 = answer_6
    answer = answer_7

    return answer
print(solution("...!@BaT#*..y.abcdefghijklm"))