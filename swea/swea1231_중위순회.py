def inOrder(v):
    # 왼쪽 자식이 있을 때
    if len(arr[v]) >= 3 :
        inOrder(int(arr[v][2]))
    # 출력
    print(arr[v][1], end = "")
    # 오른쪽 자식이 있을 때
    if len(arr[v]) ==4:
        inOrder(int(arr[v][3]))

for tc in range(1,11):
    N = int(input())

    # 2차원리스트로 인접리스트느낌으로 처리
    arr = [[]] # 0번인덱스 버리기기

    for i in range(N):
        arr.append(input().split())

    print("#{}".format(tc), end=" ")
    inOrder(1)
    print()