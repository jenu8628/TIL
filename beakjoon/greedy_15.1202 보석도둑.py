import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
arr = []  # 보석정보
bag = []  # 가방
ans = 0  # 정답
for _ in range(N):
    # M: 무게, N: 가격
    M, V = map(int, sys.stdin.readline().split())
    heapq.heappush(arr, [M, V])
for _ in range(K):
    # C: 가방 무게
    C = int(sys.stdin.readline())
    heapq.heappush(bag, C)

tem = []  # 현재 bag의 허용무게보다 작은 모든 보석들
for _ in range(K):
    capacity = heapq.heappop(bag)
    # 현재 bag의 capacity보다 이하인 모든 보석에 관하여
    while arr and capacity >= arr[0][0]:
        # 최소 무게부터 차례대로 꺼낸다
        [M, N] = heapq.heappop(arr)
        # 무게를 제외한 값만 heappush하여 넣어준다(최대힙 구성)
        heapq.heappush(tem, -N)
    # arr 최소보다는 작지만 넣을 수 있는 보석들은 있는 경우
    if tem:
        ans -= heapq.heappop(tem)
    # 남은 보석이 한 개도 없는 경우
    elif not arr:
        break
print(ans)