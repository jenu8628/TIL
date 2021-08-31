# 내풀이
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    total = []
    w_cnt = 0
    for w in range(N-2):
        for i in range(M):
            if arr[w][i] != 'W':
                w_cnt += 1
        b_cnt = 0
        for b in range(w+1, N-1):
            for j in range(M):
                if arr[b][j] != "B":
                    b_cnt += 1
            r_cnt = 0
            for r in range(b+1,N):
                for k in range(M):
                    if arr[r][k] != 'R':
                        r_cnt += 1
            total.append(w_cnt + b_cnt + r_cnt)
    print('#{} {}'.format(tc, min(total)))

# 쌤풀이
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행과열
    # 각 행에 색 카운트
    w = [0] * N
    b = [0] * N
    r = [0] * N

    for i in range(N):
        color = input()
        w[i] = color.count('W')
        b[i] = color.count('B')
        r[i] = M - w[i] - b[i]  # M개에서 w의 개수 , b의 개수를 뺀값이 r의 개수

    # 누적합 구하기 ( 나중에 한번에 계산하기 위해서 )
    for i in range(1, N):
        w[i] += w[i - 1]
        b[i] += b[i - 1]
        r[i] += r[i - 1]

    ans = N * M
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            # 흰색 칠하기
            #i까지의 전체 개수를 구한뒤 지금까지 칠해져있는 화이트 개수를 빼기
            cnt = M * (i + 1) - w[i]
            # 파란색 칠하기
            #j-i를 해서 유의미한 전체의 개수를 뽑고 , b[j] - b[i]를 하여 해당 범위의 전체 파랑 개수를 뽑아내기
            cnt += M * (j - i) - (b[j] - b[i])
            # 빨간색 칠하기
            #위와 마찬가지... ㅎ
            cnt += M * (N-1 - j) - (r[N-1] - r[j])
            ans = min(ans, cnt)
    print("#{} {}".format(tc, ans))

# 조합으로 풀기
def combination(sel, idx, cnt):
    global ans

    if cnt == 2:
        # 각각의 1이 경계를 의미하고
        w = -1
        b = -1

        for i in range(N):
            if sel[i] == 1:
                if w == -1:
                    w = i
                else:
                    b = i
        count = 0

        # 흰색영역 칠하기
        for W in range(0, w+1):
            for k in range(M):
                if flag[W][k] != 'W':
                    count += 1
        for B in range(w+1, b+1):
            for k in range(M):
                if flag[B][k] != 'B':
                    count += 1
        for R in range(b+1, N):
            for k in range(M):
                if flag[R][k] != 'R':
                    count += 1

        if count < ans:
            ans = count
        return

    if idx >= N-1:
        return

    # 경계 뽑고
    sel[idx] = 1
    combination(sel, idx+1, cnt+1)
    # 경계 초기화
    sel[idx] = 0
    combination(sel, idx+1, cnt)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]

    ans = M * N

    combination([0]*N, 0, 0)
    print('#{} {}'.format(tc, ans))