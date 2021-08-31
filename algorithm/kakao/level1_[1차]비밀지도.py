def solution(n, arr1, arr2):
    answer = []
    lis1 = []
    lis2 = []
    treasure = [[0]*n for _ in range(n)]
    for i in arr1:
        temp = []
        while i > 0:
            temp.append(i % 2)
            i = i // 2

        if len(temp) < n:
            for _ in range(n-len(temp)):
                temp.append(0)
        temp.reverse()
        lis1.append(temp)

    for i in arr2:
        temp = []
        while i > 0:
            temp.append(i % 2)
            i = i // 2
        if len(temp) < n:
            for _ in range(n-len(temp)):
                temp.append(0)
        temp.reverse()
        lis2.append(temp)
    for i in range(n):
        for j in range(n):
            if lis1[i][j] == 1:
                treasure[i][j] += 1
            if lis2[i][j] == 1:
                treasure[i][j] += 1
    for i in range(n):
        temp = ""
        for j in range(n):
            if treasure[i][j] > 0:
                temp += '#'
            elif treasure[i][j] == 0:
                temp += ' '
        answer.append(temp)

    return answer


n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(solution(n, arr1, arr2))
