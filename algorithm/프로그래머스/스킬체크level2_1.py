from itertools import permutations


def solution(numbers):
    answer = 0
    arr = list(numbers)
    temp = []
    arr2 = []
    for i in range(1, len(arr)+1):
        temp.append(list(map(''.join, permutations(arr, i))))
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if int(temp[i][j]) not in arr2:
                arr2.append(int(temp[i][j]))


    for i in arr2:
        if i == 1 or i == 0:
            continue
        check = True
        for k in range(2, i):
            if i % k == 0:
                check = False
                break
        if check:
            answer += 1
    return answer


print(solution("011"))