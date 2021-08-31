# 내풀이
T = int(input())
for tc in range(1,T+1):
    arr_list = [list(map(int,input().split())) for i in range(9)]
    result = 1
    # result는 프린트 하기 위함
    for j in range(9):
        arr_height = set()
        arr_weith = set()
        for k in range(9):
            arr_weith.add(arr_list[j][k])
            arr_height.add(arr_list[k][j])
        if len(arr_weith) != 9 or len(arr_height) != 9:
            result = 0
            break
    # total은 반복문을 탈출하기 위함
    total = 0
    for x in range(0,9,3):
        for y in range(0,9,3):
            arr_sub = set()
            for m in range(3):
                for b in range(3):
                    arr_sub.add(arr_list[m+x][b+y])
            if len(arr_sub) != 9:
                result = 0
                total = 1
        # if total: 이라고 적어도 됨!
        if bool(total) == True:
            break

    print('#{} {}'.format(tc, result))

# 쌤 풀이
def check():

    for i in range(9):
        row = [0]*10
        col = [0]*10
        for j in range(9):
            # 행검사
            num1 = sudoku[i][j]
            # 열검사
            num2 = sudoku[j][i]
            # 0, False, [], None
            # 밑에는 1, True, [12]이런 식이라면 리턴 0
            # 즉 값이 있다면!
            if row[num1]:
                return 0
            if col[num2]:
                return 0
            # 위에 걸리지 않았다면 사용했음을 표시
            row[num1] = col[num2] = 1

            if i % 3 == 0 and j % 3 ==0:
                square = [0]*10
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        num = sudoku[r][c]
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    if check():
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))