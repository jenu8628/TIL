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


left = {'1': 0, '4': 1, '7': 2, '*': 3}
right = {'3': 0, '6': 1, '9': 2, '#': 3}
mid = {'2': 0 , '5': 1, '8': 2, '0': 3}

def solution2(numbers, hand):
    answer = ''
    position = ['*', '#']   # (왼손 위치, 오른손 위치)
    for number in numbers:
        if left.get(str(number)) != None:
            answer += 'L'
            position[0] = number
        elif right.get(str(number)) != None:
            answer += 'R'
            position[1] = number
        else:

            if left.get(str(position[0])) != None:
                l_idx = left[str(position[0])]
            else:
                l_idx = mid[str(number)]

            if right.get(str(position[1])) != None:
                r_idx = right[str(position[1])]
            else:
                r_idx = mid[str(number)]

            m_idx = mid[str(number)]

            if abs(m_idx - l_idx) > abs(m_idx - r_idx):
                answer += 'R'

            elif abs(m_idx - l_idx) < abs(m_idx - r_idx):
                answer += 'L'
                position[0] = number
            elif abs(m_idx - l_idx) == abs(m_idx - r_idx):
                if hand == 'right':
                    answer += 'R'
                    position[1] = number
                else:
                    answer += 'L'
                    position[0] = number
    return answer

if __name__ == '__main__':
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
    print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
    print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))