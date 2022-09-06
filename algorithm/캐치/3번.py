def solution(s):
    answer = []
    for i in range(len(s)):
        check = ""
        for j in range(i+1, len(s)+1):
            if s[j-1] in check:
                break
            if s[i:j] not in answer:
                answer.append(s[i:j])
            check = s[i:j]
    return answer

# 중복되지 않고

# print(solution("abac"))
# print(solution("abcd"))
print(solution("zxzxz"))