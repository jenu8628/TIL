from collections import deque

def solution(info, edges):
    answer = 0
    node = [[] for _ in range(len(info))]
    for edge in edges:
        animal = info[edge[1]]
        node[edge[0]].append([edge[1], animal])

    cnt = 1 # 1번이 양
    dist = 0
    visit = list(set())
    Q = deque([0])
    while cnt > 0:
        x = Q.popleft()
        print(x)
        for i in node[x]:
            if node[i[0]] == []:
                Q.append(x)
            if (x, i[0]) not in visit:
                Q.append(i[0])
                if i[1] == 0:
                    cnt += 1
                    dist += 1
                else:
                    cnt -= 1


    print(dist)
    print(node)
    return answer



info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
solution(info, edges)