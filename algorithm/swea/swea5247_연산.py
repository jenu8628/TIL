for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visit = [0] * 1000001
    Q = [(N, 0)]
    i = 0
    visit[N] = 1
    idx = 0
    while True:
        x = Q[idx]
        idx += 1
        i = x[1] + 1
        if x[0]*2 == M or x[0] + 1 == M or x[0]-10 == M or x[0] - 1 == M:
            break
        if x[0] < M:
            if visit[x[0] * 2] == 0 and x[0] * 2 < 1000001:
                Q.append((x[0] * 2, i))
                visit[x[0] * 2] = 1

            if visit[x[0] + 1] == 0 and x[0] + 1 < 1000001:
                Q.append((x[0] + 1, i))
                visit[x[0] + 1] = 1
        if visit[x[0]-10] == 0 and 0 < x[0]-10:
            Q.append((x[0]-10, i))
            visit[x[0]-10] = 1

        if visit[x[0] - 1] == 0 and 0 < x[0] - 1:
            Q.append((x[0] - 1, i))
            visit[x[0] - 1] = 1
    print('#{} {}'.format(tc, i))

from collections import deque

def bfs():
    queue = deque()
    queue.append(N)

    ans = 0
    while queue:
        size = len(queue)

        for i in range(size):
            curr = queue.popleft()
            if curr == M: return ans
            for j in (curr + 1, curr - 1, curr * 2, curr - 10):
                if 0 < j <= 1000000 and memo[j] == -1:
                    memo[j] = 1
                    queue.append(j)
        ans += 1


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    memo = [-1] * 1000001
    print("#{} {}".format(tc, bfs()))
########################################

#2번
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10


def bfs():
    queue = [0] * 1000000
    front = rear = -1
    rear += 1
    queue[rear] = N
    while front != rear:
        front += 1
        curr_N = queue[front]
        if curr_N == M:
            return
        for i in range(4):
            next_N = calc(curr_N, i)
            if 0 < next_N <= 1000000 and memo[next_N] == -1:
                memo[next_N] = memo[curr_N]+1
                rear += 1
                queue[rear] = next_N


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    memo = [-1] * 1000001
    memo[N] = 0
    bfs()
    print("#{} {}".format(tc, memo[M]))
#####################################################

###########################################################
#1번
def calc(num, idx):
    if idx == 0:
        return num + 1
    elif idx == 1:
        return num - 1
    elif idx == 2:
        return num * 2
    else:
        return num - 10


def bfs():
    queue = [0] * 1000000
    front = rear = -1
    rear += 1
    queue[rear] = (N, 0)
    while front != rear:
        front += 1
        curr_N, curr_cnt = queue[front]
        if curr_N == M:
            return curr_cnt
        for i in range(4):
            next_N = calc(curr_N, i)
            if 0 < next_N <= 1000000:
                rear += 1
                queue[rear] = (next_N, curr_cnt + 1)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    print("#{} {}".format(tc,bfs()))
