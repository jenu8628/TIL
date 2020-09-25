def dist(a, b):
    # 북쪽
    if a == 1:
        return b
    # 남쪽
    elif a == 2:
        return X + Y + X - b
    # 서쪽
    elif a == 3:
        return X + Y + X + Y - b
    # 동쪽
    else:
        return X + b
X, Y = map(int, input().split())
N = int(input())
# 둘레의 전체 길이
circum = 2 * (X + Y)
arr = []
# 상점과 동근이의 각자 위치를 0,0 기준점으로 부터 길이로 표시함
for i in range(N+1):
    a, b = map(int, input().split())
    arr.append(dist(a, b))
# my_dist 는 동근이
my_dist = arr[-1]
ans = 0
for i in range(N):
    # 동근이와 상점의 길이차의 절댓값
    size = abs(my_dist - arr[i])
    # size: (동근이와 삼전의 길이차)
    # 전체길이에서 그 size를 뺀 값중 더 작은 값을 계속 더함
    ans += min(size, circum-size)
print(ans)