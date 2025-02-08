def can_cross(stones, k, people):
    count = 0  # 연속된 0의 개수
    for stone in stones:
        if stone < people:
            count += 1
            if count >= k:  # k 이상 연속되면 건널 수 없음
                return False
        else:
            count = 0  # 0이 연속되지 않도록 초기화
    return True  # 모든 돌을 건널 수 있음

def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1
    
    while left <= right:
        mid = (left + right) // 2
        if can_cross(stones, k, mid):
            answer = mid
            left = mid + 1  # 더 많은 인원 체크
        else:
            right = mid - 1  # 적은 인원 체크
    
    return answer
