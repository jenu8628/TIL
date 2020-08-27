T = int(input())
for test_case in range(1, T + 1):
    numbers = input().split()
    numbers_int = []
    for number in numbers:
        numbers_int.append(number)
    max_number = numbers_int[0]
    for i in numbers_int:
        if max_number < i:
            max_number = i
        print(max_number)
