N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = []

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            cnt = 0
            cnt = arr[i] + arr[j] + arr[k]
            if cnt <= M:
                arr1.append(cnt)
print(max(arr1))



# 비트연산으로 풀어보았음.
# arr2 = []
# for i in range(1<<N): # 1<<n : 부분집합의 개수
#     arr1 = []
#     for j in range(N): # 원소의 수만큼 비트를 비교함
#         if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
#             arr1.append(arr[j])
#             if len(arr1) == 3:
#                 arr2.append(arr1)
# result = [] # 더한거 받을 것임
# for i in range(len(arr2)):
#     result.append(sum(arr2[i]))

# total = []
# for i in range(len(result)):
#     if result[i] <= M:
#         total.append(result[i])
# print(max(total))

