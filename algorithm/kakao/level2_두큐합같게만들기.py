from collections import deque

def make_answer(q1, q2, half_total_sum):
    count = 0
    q1_sum = sum(q1)
    while q1 and q2:
        if q1_sum == half_total_sum:
            return count
        elif q1_sum > half_total_sum:
            q1_sum -= q1.popleft()
        else:  # q1의 합이 q2보다 작을 때
            q1.append(q2.popleft())
            q1_sum += q1[-1]
        count += 1
    return 9999999

def solution(queue2, queue1):
    total_sum = sum(queue1 + queue2)
    if total_sum % 2:
        return -1
    half_total_sum = sum(queue1 + queue2) // 2
    count1 = make_answer(deque(queue1), deque(queue2), half_total_sum)
    count2 = make_answer(deque(queue2), deque(queue1), half_total_sum)
    if count1 == 9999999 and count2 == 9999999:
        return -1
    min_count = min(count1, count2)
    return min_count

def solution2(queue2, queue1):
    total_sum = sum(queue1 + queue2)
    if total_sum % 2:
        return -1
    half_total_sum = sum(queue1 + queue2) // 2
    count1 = make_answer(deque(queue1), deque(queue2), half_total_sum)
    count2 = make_answer(deque(queue2), deque(queue1), half_total_sum)
    if count1 == 9999999 and count2 == 9999999:
        return -1
    min_count = min(count1, count2)
    return min_count



if __name__ == '__main__':
    print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
    print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
    print(solution([1, 1], [1, 5]))
    print(solution([1, 10, 1, 2], [1, 2, 1, 2]))
    # print(solution2([3, 2, 7, 2], [4, 6, 5, 1]))
    # print(solution2([1, 2, 1, 2], [1, 10, 1, 2]))
    # print(solution2([1, 1], [1, 5]))
    # print(solution2([1, 10, 1, 2], [1, 2, 1, 2]))




