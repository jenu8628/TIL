import sys
N = int(sys.stdin.readline())
dis = list(map(int, sys.stdin.readline().split()))
won = list(map(int, sys.stdin.readline().split()))
dis.append(0)

now = 999999999
cnt = 0
ans = 0
for i in range(N):
    if won[i] < now:
        now = won[i]
    ans += dis[i] * now
print(ans)