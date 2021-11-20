import sys

def graph(x):
    stack = [x]
    visit = [x]
    while stack:
        s = stack.pop()
        for i in arr[s]:
            if i not in visit:
                stack.append(i)
                visit.append(i)
    return visit

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
arr = {i: [] for i in range(1, N+1)}
for _ in range(V):
    s, e = map(int, sys.stdin.readline().split())
    arr[s].append(e)
    arr[e].append(s)
print(len(graph(1)) - 1)