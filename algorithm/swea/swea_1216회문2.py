# 내풀이
for i in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    N = 100
    number = []
    # 0~100까지 검사
    for i in range(N):
        # 회문길이를 99부터 내려오면서 검사할 예정
        for j in range(N-1, 0, -1):
            # 행 또는 열에서 회문길이만큼 움직일 거리
            for m in range(100-j+1):
                row = ''
                col = ''
                # 회문이 맞는지 검사
                for k in range(j):
                    row += arr[i][k+m]
                    col += arr[k+m][i]
                if row == row[::-1]:
                    number.append(len(row))
                if col == col[::-1]:
                    number.append(len(col))
    max_number = max(number)

    print('#{} {}'.format(tc, max_number))

# 쌤풀이
def check(M):
    for i in range(N):
        for j in range(N-M+1):
            #가로
            tmp = words[i][j:j+M]
            #세로
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0

for tc in range(10):
    tc_num = int(input())
    N = 100
    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words)) # 세로줄

    for k in range(100, 0, -1):
        ans = check(k)
        if ans != 0:
            break
    print("#{} {}".format(tc_num, ans))
