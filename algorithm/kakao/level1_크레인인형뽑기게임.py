def solution_1(board, moves):
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


def solution_2(board, moves):
    answer = 0
    bucket = []
    r_board = list(map(list, zip(*board)))
    visit = [[0] * len(board[0]) for _ in range(len(board[0]))]

    for idx in moves:
        for col, current in enumerate(r_board[idx-1]):
            if current != 0 and visit[idx-1][col] == 0:
                if len(bucket) > 0 and bucket[-1] == current:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(current)
                visit[idx-1][col] += 1
                break
    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    # print(solution_1(board, moves))
    print(solution_2(board, moves))