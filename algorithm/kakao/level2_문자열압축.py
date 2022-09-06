import sys
# 생각 1
# 문자열을 받았어
# 처음부터 확인을 해! 즉, 이어붙여봐
# 그러다가 첫글자와 같은 애를 만나면!?
# 뒤에도 똑같은지 확인을 해!
# 똑같다면 반복되는 문자야!
# 이방법은 실패! 오점이 너무 많음!

# 생각 2
# 문자열을 받았어
# 쪼개는 걸 1부터 정하고 들어가는거야
# 완전탐색같은 방법이기 때문에 될거같긴 한데 시간이 오래걸리긴할듯!
# 일단 탐색은 반복되는것을 찾는 것이기 때문에
# s//2정도 까지만 해도 됨!


def solution1(s):
    answer = 2000
    result = ""
    # 만약 s =1 이라면 당연히 answer는 1
    if len(s) == 1:
        return 1
    # 몇개를 짜를지 정하는 반복문!
    for i in range(1, len(s)//2+1):
        count = 1
        temp = s[:i]
        for j in range(i, len(s)+1, i):
            if temp == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + temp
                temp = s[j:j+i]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + temp
        if answer > len(result):
            answer = len(result)
        result = ""
    return answer

def solution2(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        temp = s[:i]
        count = 1
        min_str = ""
        for j in range(i, len(s)+1, i):
            if s[j:j+i] == temp:
                count += 1
            else:
                if count == 1:
                    count = ""
                min_str += str(count) + temp
                temp = s[j:j+i]
                count = 1
        if count == 1:
            count = ""
        min_str += str(count) + temp
        answer = min(answer, len(min_str))

    return answer


if __name__ == '__main__':
    # print(solution1("aabbaccc"))
    # print(solution1("ababcdcdababcdcd"))
    # print(solution1("abcabcdede"))
    # print(solution1("abcabcabcabcdededededede"))
    # print(solution1("xababcdcdababcdcd"))

    print(solution2("aabbaccc"))
    print(solution2("ababcdcdababcdcd"))
    print(solution2("abcabcdede"))
    print(solution2("abcabcabcabcdededededede"))
    print(solution2("xababcdcdababcdcd"))