T = int(input())
#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
for test_case in range(1, T + 1):
    numbers = input().split()
    numbers_int = []
    for number in numbers:
        numbers_int.append(int(number))
    total = 0
    for i in numbers_int:
        total += i
    avg = int(round(total / len(numbers_int),0))
    print(f'#{test_case} {avg}')