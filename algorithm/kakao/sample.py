n = 4
queries = [[0, 1], [0, 2], [0, 3], [3, 4], [1, 5], [1, 6],
           [2, 7], [1, 9], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]

queue = [[] for _ in range(n+1)]
star = 0
answer = []
for q in queries:
    if len(queue[-1]) == 0:
        queue[-1].append(q[1])
        continue
    if q[0] >= 0:
        queue[q[0]].append(q[1])
    elif q[0] < 0:
        cnt = 0
        answer.append(queue[-1].pop(0))
        while True:
            if len(queue[star]) > 0:
                queue[-1].append(queue[star].pop(0))
                star = (star+1) % n
                break
            if cnt > n:
                break
            cnt += 1
            star = (star+1) % n
print(answer)