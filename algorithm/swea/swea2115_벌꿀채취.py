def powerset(idx, tmp, max_honey, arr):
    global time
    if tmp > C:
        return
    if idx == len(arr):
        if max_honey > time:
            time = max_honey
        return
    powerset(idx+1, tmp+arr[idx], max_honey+(arr[idx] ** 2), arr)
    powerset(idx+1, tmp, max_honey, arr)

def powerset2(idx, tmp, max_honey, arr):
    global time2
    if tmp > C:
        return
    if idx == len(arr):
        if max_honey > time2:
            time2 = max_honey
        return
    powerset2(idx+1, tmp+arr[idx], max_honey+(arr[idx] ** 2), arr)
    powerset2(idx+1, tmp, max_honey, arr)

def check(r, c):
    global ans
    honey_list = []
    for i in range(M):
        visit[r][c + i] = 1
        honey_list.append(honey[r][c+i])
    powerset(0, 0, 0, honey_list)
    for i in range(N):
        for j in range(N-M+1):
            if visit[i][j] == 0:
                check2(i, j)
            if time + time2 > ans:
                ans = time + time2

def check2(r,c):
    honey_list = []
    for i in range(M):
        if visit[r][c + i] == 0:
            visit[r][c + i] = 1
            honey_list.append(honey[r][c + i])
    powerset2(0, 0, 0, honey_list)
    return

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N-M+1):
            time = 0
            time2 = 0
            check(i, j)
            visit = [[0]*N for _ in range(N)]
    print("#{} {}".format(tc, ans))


# 쌤풀이 ------------------------------------------------------------------
def choose(r,c):
    global first, second
    honey = arr[r][c:c+M]
    max_cost = 0
    for i in range(1 << M):
        sum_honey = sum_cost = 0
        for j in range(M):
            if i & (1 << j):
                sum_honey += honey[j]
                sum_cost += (honey[j]) ** 2
            if sum_honey <= C:
                max_cost = max(max_cost, sum_cost)

    if max_cost > first[0]:
        if r == first[1] and c < first[2]+M:
            first = [max_cost, r, c]
        else:
            second = first[:]
            first = [max_cost, r, c]
    elif max_cost > second[0]:
        if r != first[1] or c >= first[2]+M:
            second = [max_cost, r, c]

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 값, 행, 열
    first = [0, 0, 0]
    second = [0, 0, 0]
    #순회하면서 벌통을 뽑아보기
    for i in range(N):
        for j in range(N-M+1):
            choose(i,j)
    print("#{} {}".format(tc, first[0]+second[0]))

# 2번째 풀이 -------------------------------------------------
def calc(idx, sum_honey, sum_cost):
    global max_cost2
    if sum_honey > C:
        return
    max_cost2 = max(max_cost2, sum_cost)
    for i in range(idx, M):
        calc(i+1, sum_honey+honey2[i], sum_cost+honey2[i]**2)

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 값, 행, 열
    first = [0, 0, 0]
    second = [0, 0, 0]
    honey_list=[]
    #순회하면서 벌통을 뽑아보기
    for i in range(N):
        for j in range(N-M+1):
            honey2 = arr[i][j:j+M]
            max_cost2 = 0
            calc(0, 0, 0)
            honey_list.append((max_cost2, i, j))
    honey_list.sort(reverse=True)
    first2 = honey_list.pop(0)
    for cost, r, c in honey_list:
        if r == first2[1] and first2[2] - M < c < first2[2] + M: continue
        second2 = [cost, r, c]
        break
    print("#{} {}".format(tc, first2[0]+second2[0]))