import heapq

def solution(n, works):
    # 최대 힙을 만들기 위해 음수로 변환
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    
    # n시간 동안 작업량 줄이기
    for _ in range(n):
        if not max_heap:  # 작업이 모두 끝난 경우
            break
        max_work = -heapq.heappop(max_heap)  # 가장 큰 작업량 꺼내기
        if max_work > 0:
            max_work -= 1  # 작업량 1 줄이기
        heapq.heappush(max_heap, -max_work)  # 다시 힙에 추가
    
    # 남은 작업량의 제곱합 계산
    return sum(work ** 2 for work in max_heap)
