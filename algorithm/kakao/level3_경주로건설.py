from collections import deque

def solution(board):
    INF = 1e9
    N = len(board)
    def bfs(arr):
        graph = [[INF] * N for _ in range(N)]
        # 위 왼쪽 아래 오른쪽
        dist = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        Q = deque([arr])
        while Q:
            r, c, cost, head = Q.popleft()
            for i, (dr, dc) in enumerate(dist):
                nr = r + dr
                nc = c + dc
                n_cost = cost + 600 if i != head else cost + 100
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0 and graph[nr][nc] > n_cost:
                    graph[nr][nc] = n_cost
                    Q.append([nr, nc, n_cost, i])
        return graph[-1][-1]

    return min(bfs([0, 0, 0, 2]), bfs([0, 0, 0, 3]))

board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))