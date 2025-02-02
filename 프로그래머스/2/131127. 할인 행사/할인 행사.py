from collections import Counter

def solution(want, number, discount):
    want_dict = {item: count for item, count in zip(want, number)}
    current_window = Counter(discount[:10])  # 초기 10일간 제품 개수 저장
    
    result = 0  # 가능한 회원가입 날짜 수
    
    # 첫 윈도우가 조건을 만족하는지 체크
    if current_window == want_dict:
        result += 1
    
    # 슬라이딩 윈도우로 한 칸씩 이동하며 확인
    for i in range(10, len(discount)):
        # 앞의 요소 제거
        removed_item = discount[i - 10]
        current_window[removed_item] -= 1
        if current_window[removed_item] == 0:
            del current_window[removed_item]  # 개수가 0이 되면 삭제
        
        # 새로운 요소 추가
        added_item = discount[i]
        current_window[added_item] += 1
        
        # 현재 윈도우가 조건을 만족하는지 확인
        if current_window == want_dict:
            result += 1

    return result
