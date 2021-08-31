T = int(input())
for test_case in range(1, T + 1):
    numbers = input().split()
    numbers_int = []
    for number in numbers:
        numbers_int.append(int(number))
    numbers_int.sort()
    middle = len(numbers_int)//2
    print(numbers_int[middle])
    