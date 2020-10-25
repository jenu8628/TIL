sr = [
        '0001101', '0011001', '0010011', '0111101', '0100011',
        '0110001', '0101111', '0111011', '0110111', '0001011'
    ]
# def check(arr):
#     cnt = 0
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             cnt += arr[i] * 3
#         else:
#             cnt += arr[i]
#     if cnt % 10 == 0:
#         return sum(arr)
#     else:
#         return 0
#
# def code(arr):
#     for i in range(0, len(arr), 7):
#         cnt = 0
#         x = []
#         k = arr[0]
#         for j in range(7):
#             if arr[i:i+7][j] != k:
#                 x.append(cnt)
#                 k = arr[i:i+7][j]
#                 cnt = 0
#             cnt += 1
#             if j == 6:
#                 x.append(cnt)
#         for j in range(len(sr)):
#             if sr[j] == x:
#                 answer.append(j)
#     return answer

T = int(input())
for C in range(1,T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    answer = []
    tmp = []
    for j in range(N):
        if tmp:
            break
        for i in range(M-1, -1, -1):
            if arr[j][i] == 1:
                tmp = arr[j][i-55:i+1]
                break
    print(tmp)
    print(len(tmp))
    # print('#{} {}'.format(C, check(code(tmp))))
