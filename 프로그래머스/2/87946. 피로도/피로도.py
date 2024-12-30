from itertools import permutations

def solution(k, dungeons):
    max_explored = 0
    
    # 모든 순열을 시도
    for order in permutations(dungeons):
        current_fatigue = k
        explored_count = 0
        
        for required, cost in order:
            if current_fatigue >= required:  # 최소 필요 피로도를 만족하는 경우
                current_fatigue -= cost
                explored_count += 1
            else:
                break  # 더 이상 탐험할 수 없으면 중단
        
        max_explored = max(max_explored, explored_count)
    
    return max_explored
