from collections import deque

def solution(priorities, location):
    # 초기 큐 구성 (우선순위와 초기 인덱스를 함께 저장)
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    execution_order = 0  # 실행된 프로세스 수를 기록
    
    while queue:
        # 큐에서 첫 번째 프로세스를 꺼냄
        current = queue.popleft()
        
        # 우선순위 비교
        if any(current[0] < q[0] for q in queue):
            # 더 높은 우선순위가 있으면 다시 큐에 추가
            queue.append(current)
        else:
            # 실행 순서 증가
            execution_order += 1
            
            # 목표 프로세스가 실행된 경우
            if current[1] == location:
                return execution_order