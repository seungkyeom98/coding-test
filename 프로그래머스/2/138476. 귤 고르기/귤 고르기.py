from collections import Counter

def solution(k, tangerine):
    # 귤 크기별 빈도 계산
    frequency = Counter(tangerine)
    
    # 빈도 내림차순 정렬
    sorted_frequencies = sorted(frequency.values(), reverse=True)
    
    # 종류 수 계산
    selected_types = 0
    total_selected = 0
    
    for freq in sorted_frequencies:
        total_selected += freq
        selected_types += 1
        if total_selected >= k:
            break
    
    return selected_types

# 테스트
k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
solution(k, tangerine)
