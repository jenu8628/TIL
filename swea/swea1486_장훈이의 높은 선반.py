# 풀이 1(조합) == 모든 조합을 뽑으면 부분집합
def comb(idx, sidx, R):
    if sidx == R:
        if sum(sel) >= B:
            total.append(sum(sel))
        return

    for j in range(idx, N):
        sel[sidx] = arr[j]
        comb(j+1, sidx+1, R)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    for i in range(1, N+1):
        sel = [0] * i
        comb(0, 0, i)
    print('#{} {}'.format(tc, min(total) - B))

# 풀이 2 부분집합
def powerset(idx):
    if idx == N :
        result = 0
        for i in range(N):
            if sel[i] == 1:
                result += arr[i]
        if result >= B:
            total.append(result)
        return
    sel[idx] = 1
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    total = []
    sel = [0] * N
    powerset(0)
    print('#{} {}'.format(tc, min(total) - B))


# 쌤풀이
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 99999999999

    # 비트마스킹 형식으로 powerset
    for i in range(1, 1<<N):
        total = 0
        for j in range(N):
            if i & (1<<j):
                total += H[j]
        if total >= B and total < ans:
            ans = total
    print("#{} {}".format(tc, ans - B))