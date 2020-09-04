def BSF(x):
    visit[x] = 1
    queue = []
    queue.append(x)
    while len(queue) != 0:
        num = queue.pop(0)
        for w in range(1, 101):
            if arr[num][w] == 1 and visit[w] == 0:
                queue.append(w)
                visit[w] = visit[num] + 1

for tc in range(1, 11):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    visit = [0]*101
    # 인접행렬생성
    arr = [[0] * 101 for _ in range(101)]
    # 인접행렬 입력
    for i in range(N//2):
        st, ed = temp[2*i], temp[(2*i)+1]
        arr[st][ed] = 1
    BSF(M)
    maxI = 0
    for j in range(len(visit)):
        if visit[maxI] <= visit[j]:
            maxI = j
    print("#{} {}".format(tc, maxI))