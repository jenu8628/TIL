import sys
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.']
ALPA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def solution(new_id):
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환
    check1 = ''
    for i in new_id:
        if i in ALPA:
            check1 += alpa[ALPA.index(i)]
        else:
            check1 += i
    # 2단계
    check2 = ''
    for i in check1:
        if i in alpa:
            check2 += i
    # 3단계
    check3 = ''
    cnt = False
    for i in check2:
        if i == '.':
            if cnt == False:
                check3 += i
                cnt = True
        else:
            check3 += i
            cnt = False

    # 4단계
    check4 = ''
    for i in range(len(check3)):
        if i == 0:
            if check3[i] == '.':
                pass
            else:
                check4 += check3[i]
        elif i == len(check3) - 1:
            if check3[i] == '.':
                pass
            else:
                check4 += check3[i]
        else:
            check4 += check3[i]

    # 5단계
    check5 = ""
    if len(check4) == 0:
        check5 += 'a'
    else:
        check5 += check4

    # 6단계
    check6 = ""
    if len(check5) >= 16:
        if check5[14] == '.':
            check6 += check5[0:14]
        else:
            check6 += check5[0:15]
    else:
        check6 += check5

    # 7단계
    answer = ""
    answer += check6
    if len(check6) <= 2:
        count = 3 - len(check6)
        while count > 0:
            count -= 1
            answer += check6[-1:]
    return answer


# 아이디의 길이 3<= x <= 15
# 아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)만 사용
# 단, 마침표(.)는 처음과 끝에 사용할 수 없으며 연속사용 x
new_id = sys.stdin.readline()
print(solution(new_id))

#ASDFZXCV..._-.+12354!@#@%
#asdfasdfasdfas.fqwer