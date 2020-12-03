# 비트연산
for tc in range(1, int(input())+1):
    N, L = map(int, input().split())
    tmp = []
    for i in range(N):
        T, cal = map(int, input().split())
        tmp.append([T, cal])
    ans = 0
    for i in range(1 << N):
        cnt = 0
        test = 0
        for j in range(N):
            if (1 << j) & i:
                cnt += tmp[j][1]
                test += tmp[j][0]
                if cnt > L:
                    break
            if ans < test:
                ans = test
    print('#{} {}'.format(tc, ans))

# 재귀
def powerset(idx, cal, test):
    global ans
    if cal > L:
        return

    if idx == N:
        if test > ans:
            ans = test
        return
    powerset(idx + 1, cal + calorie[idx], test + score[idx])
    powerset(idx + 1, cal, test)

for tc in range(1, int(input())+1):
    N, L = map(int, input().split())
    score, calorie = [], []  # 점수와 칼로리
    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans = 0
    powerset(0, 0, 0)
    print("#{} {}".format(tc, ans))

# 쌤풀이
# 비트연산
for tc in range(1, int(input())+1):
    n, l = map(int, input().split())
    score, calorie = [], []
    for _ in range(n):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans = 0
    for i in range(1<<n):
        sum_score = 0
        sum_calorie = 0
        for j in range(n):
            if i & (1<<j):
                sum_calorie += calorie[j]
                sum_score += score[j]
        if sum_calorie <= l:
            ans = max(ans, sum_score)
    print('#{} {}'.format(tc, ans))


# 재귀
def cook(idx):
    global ans
    if idx >= n:
        sum_score = 0
        sum_calorie = 0
        for i in range(n):
            if sel[i]:
                sum_score += score[i]
                sum_calorie += calorie[i]
        if sum_calorie <= l:
            ans = max(ans, sum_score)
        return

    # 재료를 뽑고가고
    sel[idx] = True
    cook(idx+1)
    # 재료를 안뽑고가고
    sel[idx] = False
    cook(idx+1)

for tc in range(1, int(input())+1):
    n, l = map(int, input().split())
    score, calorie = [], []
    for _ in range(n):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans = 0
    sel = [0]*n
    cook(0)
    print('#{} {}'.format(tc, ans))

# 백트래킹
def cook(idx, sum_score, sum_calorie):
    global ans
    if sum_calorie > L:
        return
    if idx == N:
        if sum_score > ans:
            ans = sum_score
        return

    cook(idx+1, sum_score + score[idx], sum_calorie + calorie[idx])
    cook(idx+1, sum_score, sum_calorie)

for tc in range(1, int(input()) + 1):
    N, L = map(int, input().split()) # 재료, 제한칼로리
    score, calorie = [], [] # 점수와 칼로리

    for _ in range(N):
        s, c = map(int, input().split())
        score.append(s)
        calorie.append(c)
    ans=0
    cook(0, 0, 0)
    print("#{} {}".format(tc, ans))