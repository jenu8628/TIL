def solution(board, skill):
    answer = 0
    for s in range(len(skill)):
        type, r1, c1, r2, c2, degree = skill[s]
        i, j = 0, 0
        while r1 + i <= r2:
            if type == 1:
                board[r1 + i][c1 + j] -= degree
            else:
                board[r1 + i][c1 + j] += degree
            j += 1
            if c1 + j > c2:
                j = 0
                i += 1
    for i in range(len(board)):
        board[i].sort(reverse=True)
        a = list(filter(lambda x: x > 0, board[i]))
        answer += len(a)
    return answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

# a = [1, 2, 3, 4, 5]
# b = a.count(lambda x: x> 2)
# print(b)

