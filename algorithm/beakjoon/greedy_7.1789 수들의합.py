import sys
S = int(sys.stdin.readline())
ans = 0
if S == 1:
    ans +=1
else:
    for i in range(1, S):
        S -= i
        if S < 0:
            break
        elif S == 0:
            ans+=1
            break
        ans += 1
print(ans)