from collections import deque
from math import gcd

def solution(a, b, c, d):
    q = deque()
    q.append((0, 0, 0, 0))

    # d가 각 비커의 크기와 같으면 1을 리턴
    if d == a or d == b or d == c:
        return 1

    # 최대공약수가 d의 약수가 아니면 불가능
    if d % (gcd(gcd(a, b), c)) != 0:
        return -1

    dist = [0] * 100

    # d가 가장 큰 비커보다 크면 불가능
    if d > max(a, b, c):
        return -1

    visit = [[[0] * (c + 1) for _ in range(b + 1)] for _ in range(a + 1)]

    def pour(x, y, z, cnt):
        if visit[x][y][z] == 0:
            visit[x][y][z] = 1
            q.append((x, y, z, cnt))
    while q:
        # x : a물통의 물의 양, y : b물통의 물의 양, z : c물통의 물의 양
        x, y, z, cnt = q.popleft()

        # dist 최신화
        if dist[x] == 0:
            dist[x] = cnt
        if dist[y] == 0:
            dist[y] = cnt
        if dist[z] == 0:
            dist[z] = cnt

        if dist[d] != 0:
            return dist[d]
        cnt += 1

        #채우기
        pour(a, y, z, cnt)
        pour(x, b, z, cnt)
        pour(x, y, c, cnt)

        # x -> y
        water = min(x, b - y)
        pour(x - water, y + water, z, cnt)
        # x -> z
        water = min(x, c - z)
        pour(x - water, y, z + water, cnt)
        # y -> x
        water = min(y, a - x)
        pour(x + water, y - water, z, cnt)
        # y -> z
        water = min(y, c - z)
        pour(x, y - water, z + water, cnt)
        # z -> x
        water = min(z, a - x)
        pour(x + water, y, z - water, cnt)
        # z -> y
        water = min(z, b - y)
        pour(x, y + water, z - water, cnt)

        # 버리기
        pour(0, y, z, cnt)
        pour(x, 0, z, cnt)
        pour(x, y, 0, cnt)

print(solution(3, 5, 7, 1))
print(solution(3, 6, 9, 4))