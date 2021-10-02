def solution(gems):
    num = len(set(gems))
    answer = [1, len(gems)]
    start, end = 0, 0
    check = {gems[0]: 1}
    while start < len(gems) - num + 1 and end < len(gems):
        if len(check) < num:
            end += 1
            if end == len(gems):
                break
            check[gems[end]] = check.get(gems[end], 0) + 1
        else:
            answer = [start + 1, end + 1] if (end - start) < answer[1] - answer[0] else answer
            check[gems[start]] -= 1
            if check[gems[start]] == 0:
                del check[gems[start]]
            start += 1
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))