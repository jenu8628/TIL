# 6/7못풀었음 내일 다시풀기!

# N = int(input())
# arr = [[0]*2 for _ in range(N)]
# for i in range(N):
#     s, e = map(int, input().split())
#     arr[i][0] = s
#     arr[i][1] = e
# arr.sort(key=lambda x: (x[1], x[0]))
# ans = 1
# end = arr[0][1]
# for i in range(1, N):
#     if arr[i][0] >= end:
#         ans += 1
#         end = arr[i][1]
# print(ans)

# import sys
# N = int(sys.stdin.readline())
# time = [[0]*2 for _ in range(N)]
# for i in range(N):
#     s, e = map(int, sys.stdin.readline().split())
#     time[i][0] = s
#     time[i][1] = e
# time.sort(key = lambda x: (x[1], x[0]))
# cnt = 1
# end_time = time[0][1]
# for i in range(1, N):
#     if time[i][0] >= end_time:
#         cnt += 1
#         end_time = time[i][1]
# print(cnt)
