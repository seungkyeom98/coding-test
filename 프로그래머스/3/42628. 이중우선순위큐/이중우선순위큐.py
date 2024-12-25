import heapq

def solution(operations):
    min_heap = []  # 최소 힙
    max_heap = []  # 최대 힙
    entry_map = {}  # 유효성 검사를 위한 맵

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == "I":  # 숫자 삽입
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)  # 최대 힙은 음수로 저장
            entry_map[value] = entry_map.get(value, 0) + 1
        elif command == "D":  # 삭제 명령
            if value == 1:  # 최댓값 삭제
                while max_heap and entry_map[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_map[max_val] -= 1
            elif value == -1:  # 최솟값 삭제
                while min_heap and entry_map[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_map[min_val] -= 1

    # 최종 유효한 값들만 남기기
    while min_heap and entry_map[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]