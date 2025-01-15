def solution(distance, rocks, n):
    # Step 1: 바위 정렬 및 도착지점 추가
    rocks.sort()
    rocks.append(distance)
    
    # Step 2: 이진 탐색을 위한 초기화
    left, right = 1, distance
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2  # 현재 거리의 최솟값 후보
        prev = 0  # 출발 지점
        remove_count = 0  # 제거한 바위 수
        
        # Step 3: 바위 간 거리 계산 및 제거
        for rock in rocks:
            if rock - prev < mid:  # 최소 거리 유지 불가 -> 제거
                remove_count += 1
            else:
                prev = rock  # 현재 바위를 유지
        
        # Step 4: 제거한 바위 수에 따라 범위 조정
        if remove_count > n:  # 너무 많은 바위를 제거해야 함 -> mid 감소
            right = mid - 1
        else:  # mid가 성립함 -> mid 증가
            answer = mid  # 최댓값 갱신
            left = mid + 1
    
    return answer
