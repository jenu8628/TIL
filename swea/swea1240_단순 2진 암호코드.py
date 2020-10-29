secret = [
        [3, 2, 1, 1], [2, 2, 2, 1], [2, 1, 2, 2], [1, 4, 1, 1], [1, 1, 3, 2],
        [1, 2, 3, 1], [1, 1, 1, 4], [1, 3, 1, 2], [1, 2, 1, 3], [3, 1, 1, 2]
    ]
def check(arr):
    cnt = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            cnt += arr[i] * 3
        else:
            cnt += arr[i]
    if cnt % 10 == 0:
        return sum(arr)
    else:
        return 0

def code(arr):
    for i in range(0, len(arr), 7):
        cnt = 0
        x = []
        k = arr[0]
        for j in range(7):
            if arr[i:i+7][j] != k:
                x.append(cnt)
                k = arr[i:i+7][j]
                cnt = 0
            cnt += 1
            if j == 6:
                x.append(cnt)
        for j in range(len(secret)):
            if secret[j] == x:
                answer.append(j)
    return answer

T = int(input())
for C in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    tmp = []
    answer = []
    for i in range(N):
        if tmp:
            break
        if sum(arr[i]) >= 1:
            tmp = arr[i]
            for j in range(len(tmp) - 1, -1, -1):
                if tmp[j] == 1:
                    tmp = tmp[j - 55:j + 1]
                    break
    print('#{} {}'.format(C, check(code(tmp))))
