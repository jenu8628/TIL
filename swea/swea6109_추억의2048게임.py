# from collections import deque
#
# def push():
#     if S == 'up':
#         # 열 우선순회
#         for i in range(N):
#             queue = deque()
#             for j in range(N):
#                 if tile[j][i]:
#                     queue.append(tile[j][i])
#                     tile[j][i] = 0
#             # 가장 위에부터 채워 나가기
#             idx = 0
#             while queue:
#                 if len(queue) > 1:
#                     a, b = queue.popleft(), queue.popleft()
#                     if a == b:
#                         tile[idx][i] = a + b
#                     else:
#                         tile[idx][i] = a
#                         queue.appendleft(b)
#                     idx += 1
#                 else:
#                     tile[idx][i] = queue.popleft()
#     elif S == 'down':
#         # 열 역 우선순회
#         for i in range(N):
#             queue = deque()
#             for j in range(N-1, -1, -1):
#                 if tile[j][i]:
#                     queue.append(tile[j][i])
#                     tile[j][i] = 0
#             # 가장 위에부터 채워 나가기
#             idx = N-1
#             while queue:
#                 if len(queue) > 1:
#                     a, b = queue.popleft(), queue.popleft()
#                     if a == b:
#                         tile[idx][i] = a + b
#                     else:
#                         tile[idx][i] = a
#                         queue.appendleft(b)
#                     idx -= 1
#                 else:
#                     tile[idx][i] = queue.popleft()
#     elif S == 'left':
#         # 행 우선순회
#         for i in range(N):
#             queue = deque()
#             for j in range(N):
#                 if tile[i][j]:
#                     queue.append(tile[i][j])
#                     tile[i][j] = 0
#             idx = 0
#             while queue:
#                 if len(queue) > 1:
#                     a, b = queue.popleft(), queue.popleft()
#                     if a == b:
#                         tile[i][idx] = a+b
#                     else:
#                         tile[i][idx] = a
#                         queue.appendleft(b)
#                     idx += 1
#                 else:
#                     tile[i][idx] = queue.popleft()
#     else:
#         # 행 역 우선순회
#         for i in range(N):
#             queue = deque()
#             for j in range(N-1, -1, -1):
#                 if tile[i][j]:
#                     queue.append(tile[i][j])
#                     tile[i][j] = 0
#             idx = N-1
#             while queue:
#                 if len(queue) > 1:
#                     a, b = queue.popleft(), queue.popleft()
#                     if a == b:
#                         tile[i][idx] = a + b
#                     else:
#                         tile[i][idx] = a
#                         queue.appendleft(b)
#                     idx -= 1
#                 else:
#                     tile[i][idx] = queue.popleft()
#
# for tc in range(1, int(input())+1):
#     # 한변의 길이, 방향명령어
#     N, S = input().split()
#     # 정수화
#     N = int(N)
#     tile = [list(map(int, input().split())) for _ in range(N)]
#     push()
#
#     print("#{}".format(tc))
#     for i in range(N):
#         # for j in range(N):
#             # print(tile[i][j], end=" ")
#         print(*tile[i])

# 다른 풀이 ----------------------------------------------------------------

def push():
    for i in range(N):
        stack = []
        for j in range(N-1, -1, -1):
            if tile[j][i]:
                stack.append(tile[j][i])
                tile[j][i] = 0
        # 가장 위에부터 채워 나가기
        idx = 0
        while stack:
            if len(stack) > 1:
                a, b = stack.pop(), stack.pop()
                if a == b:
                    tile[idx][i] = a + b
                else:
                    tile[idx][i] = a
                    stack.append(b)
                idx += 1
            else:
                tile[idx][i] = stack.pop()

def spin(arr):
    tmp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            tmp[i][j] = arr[N-1-j][i]
    return tmp

direction = ['up', 'left', 'down', 'right']

for tc in range(1, int(input())+1):
    # 한변의 길이, 방향명령어
    N, S = input().split()
    # 정수화
    N = int(N)
    tile = [list(map(int, input().split())) for _ in range(N)]
    if S == 'up':
        push()
    elif S == 'left':
        tile = spin(tile)
        push()
        tile = spin(tile)
        tile = spin(tile)
        tile = spin(tile)
    elif S == 'down':
        tile = spin(tile)
        tile = spin(tile)
        push()
        tile = spin(tile)
        tile = spin(tile)
    else:
        tile = spin(tile)
        tile = spin(tile)
        tile = spin(tile)
        push()
        tile = spin(tile)
    # for i in range(direction.index(S)):
    #     tile = spin(tile)
    # push()
    # if S != 'up':
    #     for i in range(4 - direction.index(S)):
    #         tile = spin(tile)
    print("#{}".format(tc))
    for i in range(N):
        print(*tile[i])