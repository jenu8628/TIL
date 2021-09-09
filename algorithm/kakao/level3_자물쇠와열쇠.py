def solution(key, lock):
    M, N = len(key), len(lock)
    # 자물쇠 + 열쇠 크기만큼 확장!
    board = [[0]*(M*2 + N) for _ in range(M*2 + N)]

    # 자물쇠 중앙 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    rotated_key = key
    # 열쇠 돌리기
    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for r in range(1, M+N):
            for c in range(1, M+N):
                # 열쇠 넣어보기
                attach(r, c, M, rotated_key, board)
                # lock 기능 check
                if check(board, M, N):
                    return True
                # 열쇠 빼기
                detach(r, c, M, rotated_key, board)
    return False

def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False
    return True

def attach(r, c, M, key, board):
    for i in range(M):
        for j in range(M):
            board[r+i][c+j] += key[i][j]

def detach(r, c, M, key, board):
    for i in range(M):
        for j in range(M):
            board[r+i][c+j] -= key[i][j]

# 90도 회전 함수 zip으로 구현
def rotate(arr):
    return list(zip(*arr[::-1]))

# 90도 회전 함수 반복문
# def rotate(arr):
#     turn = [[0]*len(arr) for _ in range(len(arr))]
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             turn[i][j] = arr[len(arr)-j-1][i]
#     return turn


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
print(key)
# print(rotate(key))


# 123
# 456
# 789