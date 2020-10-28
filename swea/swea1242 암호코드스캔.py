# import sys
# sys.stdin = open('sample_input.txt', 'r')

num = ['A', 'B', 'C', 'D', 'E', 'F']
secret = [
        [3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
        [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]
    ]
def binary(x):
    tmp = []
    while x > 0:
        tmp.append(x % 2)
        x = x//2
    while len(tmp) < 4:
        tmp.append(0)
    return tmp[::-1]

def check(arr):
    tmp = []
    number = arr[0]
    cnt = 0
    for i in range(0, len(arr), (len(arr)//56)*7):
        for j in range((len(arr)//56)*7):
            if arr[i+j] == number:
                cnt += 1
            else:
                tmp.append(cnt//(len(arr)//56))
                number = arr[i+j]
                cnt = 1
            if i + j == len(arr) - 1:
                tmp.append(cnt//(len(arr)//56))
    print(tmp)
    last = []
    for i in range(0, len(tmp), 4):
        x = secret.index(tmp[i:i+4])
        last.append(x)

    sum_number = 0
    for i in range(len(last)):
        if i % 2 == 0:
            sum_number += last[i] * 3
        else:
            sum_number += last[i]
    if sum_number % 10 == 0:
        return sum(last)
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    didi = []
    answer = 0
    ans = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != '0':
                if arr[i][j] in num:
                    didi.extend(binary(num.index(arr[i][j]) + 10))
                else:
                    didi.extend(binary(int(arr[i][j])))

        if ans != didi and didi != []:
            ans = didi[:]
            tmp = []
            if len(ans) % 56 > 10:
                continue
            else:
                if len(ans) % 56 == 0 and len(ans) != 0:
                    x = len(ans)
                else:
                    x = len(ans) - len(ans) % 56
                for k in range(len(ans)-1, -1, -1):
                    if ans[k] == 1:
                        if k - (x - 1) < 0:
                            for n in range((x-1)-k):
                                tmp.append(0)
                            tmp.extend(ans[0:k + 1])
                        else:
                            tmp.extend(ans[k-(x-1):k + 1])
                        break
                print(tmp)
                answer += check(tmp)
                print(answer)
            didi = []
    print('#{} {}'.format(tc, answer))