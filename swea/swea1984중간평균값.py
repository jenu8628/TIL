# max(), min()을 사용하여 remove해서 평균구하거나
# sort()를 통해 양옆을 제외한 나머지 숫자의 평균을 구하기
T = int(input())
for tc in range(1,T+1):
    number = list(map(int, input().split()))
    # 최대 최소 빼기위해 sort()해줌
    number.sort()
    # 정렬된 number의 양옆을 제외
    # 평균을 구하고 round를 통해 소숫점 1의자리에서 반올림
    # int형태로 변환
    aver_number = int(round(sum(number[1:9])/8, 0))
    print('#{} {}'.format(tc, aver_number))