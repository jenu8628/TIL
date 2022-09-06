def solution(N, sequence):
    answer = 0
    location = 1
    for i in range(N):
        dist = abs(location - sequence[i])
        if dist > N // 2:
            dist = N - dist
        answer += dist
        location = sequence[i]
    return answer

# 집을 돌기위한 최단거리 테스트 다맞춤
print(solution(5, [1,2,3,4,5]))
print(solution(5, [3,5,4,1,2]))
