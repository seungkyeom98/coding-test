from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 위에 있는 트럭을 표현하는 큐
    bridge = deque([0] * bridge_length)
    current_weight = 0  # 현재 다리 위의 트럭 무게
    time = 0  # 경과 시간
    
    # 대기 트럭 큐
    trucks = deque(truck_weights)
    
    while trucks or current_weight > 0:
        time += 1
        
        # 다리에서 트럭 하나가 나감
        outgoing_truck = bridge.popleft()
        current_weight -= outgoing_truck
        
        if trucks:
            # 새로운 트럭이 다리에 올라갈 수 있는지 확인
            if current_weight + trucks[0] <= weight:
                incoming_truck = trucks.popleft()
                bridge.append(incoming_truck)
                current_weight += incoming_truck
            else:
                # 트럭이 올라갈 수 없으면 다리에 빈 공간 유지
                bridge.append(0)
    
    return time