T = int(input())
for tc in range(1,T+1):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n, k = map(int, input().split())
    result = 0
    for i in range(1<<len(arr)):
        sum_k = 0
        cnt = 0
        for j in range(len(arr)+1):            
            if i & (1<<j):
                sum_k += arr[j]
                cnt += 1
        if sum_k == k and cnt == n:
            result += 1
    print(f'#{tc} {result}')



        
    # for i in range(0,len(result)):
    #     if len(result[i]) == n:
    #         sub.append(result[i])
    # for i in range(0,len(sub)):
    #     if sum(sub[i]) == k:
    #         sub_k.append()
    # if sub_k == []:
    #     print(f'#{tc} 0')
    # print(f'#{tc} {len(sub_k)}')