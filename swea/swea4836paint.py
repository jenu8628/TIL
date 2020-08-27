# 10 by 10 0이 담긴 행렬을 만든다
# from pprint import pprint
# 빨간색에 색칠된 부분은 +1 해주고
# 파란색에 색칠된 부분은 +2 해주고
# 마지막으로 +3이상이 된 부분을 count한다.
T = int(input())
for tc in range(1,T+1):
    arr = [[0 for low in range(10)]for col in range(10)]
    squer = int(input())
    # 리스트 여러개 받아서 2차원리스트로 환원
    for i in range(1,squer+1):
        number = list(map(int, input().split()))
        x =number[0]
        y = number[1]
        dx = number[2]-number[0]
        dy = number[3]-number[1]
        for j in range(dx+1):
            for k in range(dy+1):
                arr[x+j][y+k] += number[4]
    cnt = 0
    for lists in arr:
        for m in lists:
            if m >=3 :
                cnt+=1 
    print(f'#{tc} {cnt}')
