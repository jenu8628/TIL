T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    total = []
    if N < M:
        for i in range(M-N+1):
            result = 0
            for j in range(N):
                result += A[j] * B[i+j]
            total.append(result)

    elif M < N:
        for k in range(N-M+1):
            result = 0
            for m in range(M):
                result += A[k+m] * B[m]
            total.append(result)
    max_total = max(total)
    print('#{} {}'.format(tc, max_total))