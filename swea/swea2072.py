T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    #numbers = input().split()
    #numbers_int = []
    #for number in numbers:
    #    numbers_int.append(int(number))
    
    # 담긴 수를 하나하나 봐서 홀수이면 total에 더한다
    total = 0
    numbers = map(int, input().split())
    #['1', '2', '3']
    #[int('1'), int('2'), int('3')]
    for number in numbers:
        if (number % 2) == 1:
            total += number
    print(f'#{test_case} {total}')
