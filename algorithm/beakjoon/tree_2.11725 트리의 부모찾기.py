import sys

def dfs(start):
    stack = [start]
    parent = [[] for _ in range(N + 1)]
    while stack:
        node = stack.pop()
        for i in graph[node]:
            parent[i].append(node)
            stack.append(i)
            graph[i].remove(node)
    return parent

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in dfs(1)[2:]:
    print(*i)

