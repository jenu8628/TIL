# import copy
# def spin(arr):
#     for i in range(N):
#         for j in range(N):
#             tmp[i][j] = arr[-(j + 1)][i]
#             ans.append(tmp[i][j])
#
# for tc in range(1,int(input())+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     tmp = copy.deepcopy(arr)
#     ans = []
#     for k in range(3):
#         spin(arr)
#         arr = copy.deepcopy(tmp)
#     print('#{}'.format(tc))
#     for k in range(0, N*N, N):
#         for i in range(k, len(ans), N*N):
#             for j in range(i, i+N):
#                 print(ans[j], end='')
#             print(end=' ')
#         print()
arr = [9,2,4,5,0,0,1,2,4,5]
arr.sort()
print(arr)
