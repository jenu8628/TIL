T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    result = []
    for i in range(N):
        cnt = 0
        for j in range(i,N):
            if arr[i] == arr[j]:
                cnt += 1
        result.append(cnt)
    max_number = -1
    max_count = -1
    for i in result:

