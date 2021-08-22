import sys
N = int(sys.stdin.readline())
# 무게 리스트로 받기
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()
# 정답
ans = 1
for i in weight:
    # 만약 정답이 i보다 작으면 바로 break
    if ans < i:
        break
    # 아니라면 계속 정답에 i를 더해준다.
    ans += i
    # ans에 게속 i를 더하며 쌓아주는데 ans가 i보다 크다면 그 안에있는 수들은
    # 다 만들 수 있다.
print(ans)