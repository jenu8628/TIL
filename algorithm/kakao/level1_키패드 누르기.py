import sys
# numbers = list(map(int, sys.stdin.readline().split()))
# hand = sys.stdin.readline()
left = [1, 4, 7, 10]
right = [3, 6, 9, 12]
mid = [2, 5, 8, 0, 11]

def solution(numbers, hand):
    answer = ''
    right_loc = 12
    left_loc = 10
    for num in numbers:
        if int(num) == 0:
            num = 11
        if left_loc in left:
            left_dic = (abs((int(num) - (left_loc + 1))) // 3) + 1
        else:
            left_dic = abs((int(num) - left_loc)) // 3

        if right_loc in right:
            right_dic = (abs((int(num) - (right_loc - 1))) // 3) + 1
        else:
            right_dic = abs((int(num) - right_loc)) // 3

        if int(num) in left:
            left_loc = int(num)
            answer += 'L'
        elif int(num) in right:
            right_loc = int(num)
            answer += 'R'
        else:
            if left_dic < right_dic:
                answer += "L"
                left_loc = int(num)
            elif left_dic > right_dic:
                answer += "R"
                right_loc = int(num)
            elif left_dic == right_dic:
                if hand == "right":
                    answer += 'R'
                    right_loc = int(num)
                else:
                    answer += "L"
                    left_loc = int(num)
    return answer

numbers = list(map(int, input().split()))
hand = input()
print(solution(numbers, hand))