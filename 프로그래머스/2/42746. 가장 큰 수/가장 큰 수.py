from functools import cmp_to_key

def solution(numbers):
    # 비교 함수 정의: 두 문자열 숫자를 이어붙였을 때 더 큰 순서를 기준으로 정렬
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0
    
    # 숫자 리스트를 문자열 리스트로 변환
    numbers_str = list(map(str, numbers))
    
    # 사용자 정의 정렬을 이용해 가장 큰 순서로 정렬
    sorted_numbers = sorted(numbers_str, key=cmp_to_key(compare))
    
    # 결과를 이어붙이고, 0으로만 구성된 경우 '0'을 반환
    result = ''.join(sorted_numbers)
    return result if result[0] != '0' else '0'