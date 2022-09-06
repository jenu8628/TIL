def solution(numbers):
    answer = 0
    for number in range(1, 10):
        if number not in numbers:
            answer += number

    return answer

if __name__ == '__main__':
    print(solution([1,2,3,4,6,7,8,0]))