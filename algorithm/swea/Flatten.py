import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, 11):
    dump = int(input())
    number = list(map(int, input().split()))
    for i in range(1, dump+1):
        max_number = max(number)
        min_number = min(number)
        if max_number > min_number + 1:
            number[number.index(max_number)] = max_number - 1
            number[number.index(min_number)] = min_number + 1
        elif max_number <= min_number + 1:
            break
    max_number = max(number)
    min_number = min(number)
    print(f'#{test_case} {max_number - min_number}')