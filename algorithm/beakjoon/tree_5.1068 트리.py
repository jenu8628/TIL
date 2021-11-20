import sys
from collections import deque

def del_tree(x):
    Q = deque([x])
    del_list = [x]
    if tree[x][0] != -1:
        tree[tree[x][0]].remove(x)
    while Q:
        v = Q.popleft()
        for i in tree[v][1:]:
            Q.append(i)
            del_list.append(i)
    return del_list

N = int(sys.stdin.readline())
tree = [[-3] for _ in range(N)]
temp = list(map(int, sys.stdin.readline().split()))
d = int(sys.stdin.readline())
for i in range(len(temp)):
    tree[i][0] = temp[i]
    if temp[i] != -1:
        tree[temp[i]].append(i)
lis = del_tree(d)
ans = 0
for i in range(len(tree)):
    if i in lis:
        continue
    if len(tree[i]) == 1:
        ans += 1
print(ans)

# 5
# -1 2 3 4 0
# 4