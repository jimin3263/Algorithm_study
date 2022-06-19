from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = [0] * bridge_length
    answer = 0
    while (bridge):
        bridge.pop(0)
        if (truck_weights):
            if (sum(bridge) + truck_weights[0] <= weight):
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
        answer += 1

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))