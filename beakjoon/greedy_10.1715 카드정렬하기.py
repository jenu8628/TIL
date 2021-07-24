import heapq

N = int(input())
if N == 1:
    int(input())
    print(0)
else:
    cards = []
    for _ in range(N):
        x = int(input())
        heapq.heappush(cards, x)
    ans = 0

    while True:
        A = heapq.heappop(cards)
        B = heapq.heappop(cards)
        ans += A+B
        if len(cards) == 0:
            break
        heapq.heappush(cards, A+B)
    print(ans)