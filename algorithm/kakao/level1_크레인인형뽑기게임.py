def solution(board, moves):
    answer = 0
    board_T = list(map(list, zip(*board)))
    basket = []
    visit = [[0]*len(board[0]) for _ in range(len(board[0]))]
    for i in moves:
        for j in range(len(board_T[i-1])):
            if board_T[i-1][j] != 0 and visit[i-1][j] == 0:
                if len(basket) != 0 and basket[-1] == board_T[i-1][j]:
                    answer += 2
                    basket.pop(-1)
                else:
                    basket.append(board_T[i-1][j])
                visit[i-1][j] += 1
                break
    return answer