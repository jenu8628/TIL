import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    numbers = input().split()
    numbers_int = []
    for number in numbers:
        numbers_int.append(int(number))
    if numbers_int[0] < numbers_int[1]:
        print(f'#{test_case} <')
    elif numbers_int[0] == numbers_int[1]:
        print(f'#{test_case} =')
    else:
        print(f'#{test_case} >')