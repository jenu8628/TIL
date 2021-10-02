from collections import deque

def move(cur1, cur2, board):
    r, c  = 0, 1
    cand = []
    # 평행이동
    parallel = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dr, dc in parallel:
        n1 = (cur1[r] + dr, cur1[c] + dc)
        n2 = (cur2[r] + dr, cur2[c] + dc)
        if check(n1[r], n1[c]) and check(n2[r], n2[c]):
            cand.append((n1, n2))
    # 회전
    if cur1[r] == cur2[r]:  # 가로방향
        U, D = -1, 1
        for d in [U, D]:
            print()
    return cand


def solution(board):
    answer = 0
    inf = 1e9
    graph = [[inf]*len(board) for _ in range(len(board))]
    new_board = [[1] * (len(board) + 2) for _ in range(len(board) + 2)]
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = 1
    Q = deque([[(1, 1), (1, 2), 0]])
    confirm = set([((1, 1), (1, 2))])
    while Q:
        cur1, cur2, count = Q.popleft()
        if cur1 == (len(board), len(board)) or cur2 == (len(board), len(board)):
            return count
        # for nxt in move(cur1, cur2, new_board):
    return answer

def check(r, c):
    if board[r][c] == 1:
        return False
    if board[r][c] == 0:
        return True

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))