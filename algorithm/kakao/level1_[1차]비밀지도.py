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


def solution2(n, arr1, arr2):
    maze1 = []
    maze2 = []
    answer = []
    for i in range(n):
        bin_1 = str(format(arr1[i], 'b'))
        bin_2 = str(format(arr2[i], 'b'))
        if len(bin_1) != n:
            bin_1 = ((n-len(bin_1)) * '0') + bin_1
        if len(bin_2) != n:
            bin_2 = ((n - len(bin_2)) * '0') + bin_2
        maze1.append(bin_1)
        maze2.append(bin_2)
    for i in range(n):
        temp = ''
        for j in range(n):
            if maze1[i][j] == '1' or maze2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer


if __name__ == '__main__':
    # print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    # print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
    print(solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution2(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))