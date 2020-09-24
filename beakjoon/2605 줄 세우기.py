N = int(input())
arr = [i for i in range(1, N+1)]
num = list(map(int, input().split()))
for i in range(N):
    # 0이면 스왑할 필요가 없으므로 pass.
    if num[i] != 0:
        # 0이 아니면 주어진 숫자만큼 swap을 진행한다.
        for k in range(num[i]):
            # 주어진 인덱스에서 부터 앞으로 swap진행!
            arr[i-k], arr[i-1-k] = arr[i-1-k], arr[i-k]
# 리스트 출력법 두가지
# print(*arr)
for i in arr:
    print(i, end=" ")

