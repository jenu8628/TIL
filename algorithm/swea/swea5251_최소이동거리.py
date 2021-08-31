def dijstra():
    # p = [None] * (V+1)
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    dist[0] = 0

    for _ in range(V):
        minIdx = -1
        min = 987654321
        for i in range(V + 1):
            if not visited[i] and min > dist[i]:
                min = dist[i]
                minIdx = i
        visited[minIdx] = True
        for j in range(V + 1):
            if not visited[j] and dist[j] > adj[minIdx][j] + dist[minIdx]:
                dist[j] = adj[minIdx][j] + dist[minIdx]
                # p[j] = minIdx
    return dist[V]


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w

    print("#{} {}".format(tc, dijstra()))


####################################################################
import heapq

def dijstra():
    # p = [None] * (V+1)
    dist = [987654321] * (V + 1)
    visited = [False] * (V + 1)
    heap = []
    #가중치와 인덱스
    heapq.heappush(heap,(0,0))
    dist[0] = 0

    while heap:
        w, v = heapq.heappop(heap)

        if not visited[v]:
            visited[v] = True
            dist[v] = w
            for i in range(V+1):
                if not visited[i] and (dist[i] > dist[v]+adj[v][i]):
                    heapq.heappush(heap, (dist[v]+adj[v][i], i))


    return dist[V]

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    adj = [[987654321] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = w

    print("#{} {}".format(tc, dijstra()))
