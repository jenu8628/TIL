# T = 테스트 케이스 개수
T = int(input())

# N * N 배열의 테두리를 특정 수 n으로 채우는 함수 (loop = idx번째 반복)
def border(N, n, loop):

    for i in range(N):
        arr[i + loop][loop] = n
        arr[loop][i + loop] = n
        arr[len(arr) - loop - 1][i + loop] = n
        arr[i + loop][len(arr) - loop - 1] = n

for tc in range(1, T + 1):

    # N = 배열의 크기, M = 첫번째 입력값, D = 변경 값
    N, M, D = map(int, input().split())
    # N * N 배열을 0으로 초기화해서 생성
    arr = [[0] * N for _ in range(N)]
    # 초기값 입력
    arr[N // 2][N // 2] = M

    # 배열에 들어갈 값들 저장할 list
    values = []
    # N은 홀수이기 때문에 2로 나눈 몫의 크기만큼 더 들어갈 수 구하기
    for i in range(1, N // 2 + 1):
        values.append(M + D * i)

    # 루프를 반복하는 숫자 (여러 곳에 사용)
    idx = 0
    # 반복문을 이용하여 숫자 채우기
    for i in range(N, 1, -2):
        border(i, values[-idx - 1], idx)
        idx += 1

    # 출력
    print('#{}'.format(tc), end=" ")
    for a in arr:
        print(sum(a), end=" ")
    print()