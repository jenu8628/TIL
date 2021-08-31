import sys

alpa = ["zero", "one", "two", "three", 'four', 'five',
        'six', 'seven', 'eight', 'nine']
alpa_A = ['z', 'o', 't', 'f', 's', 'e', 'n']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def solution(s):
    answer = ""
    result = ""
    ans = 0
    for i in range(len(s)):
        if result in alpa:
            answer += str(alpa.index(result))
            result = ""
        if s[i] in number:
            answer += s[i]
        else:
            result += s[i]
    if result in alpa:
        answer += str(alpa.index(result))
    for i in range(len(answer)):
        ans += int(answer[-(i+1)]) * (10**i)
    return ans

# s = sys.stdin.readline()
s = input()
print(solution(s))
