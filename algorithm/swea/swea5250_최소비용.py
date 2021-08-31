dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs2():
    queue = [(0, 0)]
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            power = 0 if arr[nr][nc] - arr[r][c] <= 0 else arr[nr][nc] - arr[r][c]

            if dist[nr][nc] > dist[r][c] + power + 1:
                dist[nr][nc] = dist[r][c] + power + 1
                queue.append((nr, nc))


def bfs():
    queue = [0] * 100000
    front = 0
    tail = 1
    queue[0] = (0, 0)

    while front != tail:
        r, c = queue[front]
        front += 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                tmp = 0
                if arr[nr][nc] - arr[r][c] > 0:
                    tmp = arr[nr][nc] - arr[r][c]

                if dist[nr][nc] > dist[r][c] + tmp + 1:
                    queue[tail] = (nr, nc)
                    dist[nr][nc] = dist[r][c] + tmp + 1
                    tail += 1


for tc in range(1, int(input()) + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]

    dist[0][0] = 0

    bfs()
    print("#{} {}".format(tc, dist[N - 1][N - 1]))

########################################################
import heapq
dr = [-1,1,0,0]
dc = [0,0,-1,1]


def dijkstra():
    global N, dist
    heap = []
    dist[0][0] = 0
    heapq.heappush(heap, (dist[0][0], 0, 0))
    while heap:
        curr_w, curr_r, curr_c = heapq.heappop(heap)   #weight, r, c
        for i in range(4):
            nr = curr_r+dr[i]
            nc = curr_c+dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                add_cost = arr[nr][nc] - arr[curr_r][curr_c]
                if add_cost < 0:
                    add_cost = 0
                new_weight = curr_w + 1 + add_cost
                if dist[nr][nc] > new_weight:
                    dist[nr][nc] = new_weight
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))
    return dist[N - 1][N - 1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    dist = [[987654321] * (N) for _ in range(N)]
    arr = [list(map(int,input().split())) for _ in range(N)]
    print("#{} {}".format(tc, dijkstra()))
