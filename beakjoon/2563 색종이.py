N = int(input())
# 요소가 0 인 100 X 100 행렬 만들기
arr = [[0] * 100 for _ in range(100)]
for i in range(N):
    # 색종이 위치 받기
    a, b = map(int, input().split())
    for j in range(10):
        for k in range(10):
            # 색종이 위치에 해당하는 부분에 1을 넣어준다.
            arr[a+j][b+k] = 1
cnt = 0
for i in range(100):
    # 리스트를 돌면서 1의 개수를 샌다.
    cnt += arr[i].count(1)
print(cnt)
