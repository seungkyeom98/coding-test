import re

def solution(s):
    # 문자열에서 숫자 집합들을 추출하여 리스트로 변환
    sets = sorted(
        [set(map(int, re.findall(r'\d+', group))) for group in re.findall(r'\{([\d,]+)\}', s)],
        key=len
    )
    
    result = []
    seen = set()  # 이미 추가된 원소를 추적
    
    for group in sets:
        for num in group:
            if num not in seen:
                result.append(num)
                seen.add(num)
    
    return result
