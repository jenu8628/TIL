from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리 위의 트럭을 표현하기 위함
    trucks_on_bridge = [0] * bridge_length
    # 000000000 이란 다리를 놓고 트럭을 오른쪽에 넣고
    # 쭉쭉 진행시키는 거임
    # 근데 다리용량 초과하면 기존 트럭은 왼쪽으로 한칸, 끝에 0을 다시 삽입하는거임
    truck_weights = deque(truck_weights)
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.popleft())
            else:
                trucks_on_bridge.append(0)
    return answer

print(solution(2, 10, [7,4,5,6]))