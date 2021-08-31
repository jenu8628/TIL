# 1. 가게를 몇개, 어디를 정해서 구할지 선택!
# 2. 선택된 가게에 맞게 최소금액 구하기!
# 3. 그 중 최솟값 구하기!

# 경우의 수에 따라 가게를 어떻게 고를지에 대한 조합함수
def comb(idx, sidx):
    if sidx == R:
        tmp = sel[:]
        comb_pos.append(tmp)
        return
    if idx == shop:
        return
    sel[sidx] = pos[idx]
    comb(idx+1, sidx+1)
    comb(idx+1, sidx)

# 가게에 따라 배달거리 비용을 알려주는 함수
def dis(r):
    tmp = 0
    for i in range(len(arr1)):
        min_dis = []
        for j in range(len(r)):
            # 가게 위치에 따라 배달거리를 구함
            x = abs(r[j][0] - arr1[i][0])
            y = abs(r[j][1] - arr1[i][1])
            min_dis.append(x+y)
        # 배달거리중에 최소거리를 tmp에 더함
        tmp += min(min_dis)
    return tmp

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # shop : 가게의 개수
    shop = 0
    # 입력을 받을 배열
    arr = []
    # 1의 위치 배열
    arr1 = []
    # 가게위치 배열
    pos = []
    # 배열을 받으면서 가게가 총 몇개 있는지 어디에있는지 확인
    for i in range(N):
        arr.append(list(map(int, input().split())))
        for j in range(N):
            if arr[i][j] > 1:
                shop += 1
                pos.append((i, j))
            if arr[i][j] == 1:
                arr1.append((i,j))
    # 몇개의 가게를 선택할 건지 여부
    value = []
    for i in range(1, shop+1):
        # 선택된 개수 만큼 조합 만들기!
        comb_pos = []
        R = i
        sel = [0] * R
        comb(0, 0)
        # 뽑힌 가게 개수만큼 최소비용 구하기
        for j in range(len(comb_pos)):
            n = 0
            for k in range(len(comb_pos[j])):
                # 운용비를 계속 더해줌
                n += arr[comb_pos[j][k][0]][comb_pos[j][k][1]]
            # tmp(배달거리)와 n(운용비)의 합을 value에 append해줌
            value.append(dis(comb_pos[j])+n)
    # 총합중에 가장 작은 값을 출력
    print('#{} {}'.format(tc, min(value)))