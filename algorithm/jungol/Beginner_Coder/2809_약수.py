while True:
    N = int(input())
    # 제곱근 구하기
    # 약수에서 제곱근은 중앙 기준점이 되기 때문!
    square = int(N**(1/2))
    ans = []
    for i in range(1, square+1):
        # i가 약수라면
        if N % i == 0:
            # 정답에 추가!
            ans.append(i)
            # i가 약수이면 i * x = N임!
            # 따라서 x도 추가해줘야함!
            # 그런데 제곱근은 중복하지 말아야 하므로!
            # 제곱근이아니라면!
            if N // i != i:
                # 정답에추가!
                ans.append(N//i)
    # 낮은숫자부터 정렬!
    ans.sort()
    print(*ans)