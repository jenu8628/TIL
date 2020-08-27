T = int(input())
import copy
for tc in range(1, T+1):
    N = int(input())
    number = [list(map(int, input().split())) for _ in range(N)]
    # 90도 회전
    result0 = copy.deepcopy(number)
    for i in range(N):
        for j in range(N):
            result0[i][j] = number[-(j+1)][i]
    # 180도 회전
    result1 = copy.deepcopy(result0)
    for i in range(N):
        for j in range(N):
            result1[i][j] = result0[-(j+1)][i]
    # 270도 회전
    result2 = copy.deepcopy(result1)
    for i in range(N):
        for j in range(N):
            result2[i][j] = result1[-(j+1)][i]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(result0[i][j], end = '')
        print(end = ' ')
        for k in range(N):
            print(result1[i][k], end = '')
        print(end=' ')
        for n in range(N):
            print(result2[i][n], end='')
        print()
