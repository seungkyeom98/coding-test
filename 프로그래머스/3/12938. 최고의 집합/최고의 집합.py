def solution(n, s):
    if n > s:
        return [-1]
    
    # 기본 값 x와 나머지
    x = s // n
    remainder = s % n
    
    # 나머지 만큼 1을 더해주고 나머지는 x로 채운다
    result = [x] * (n - remainder) + [x + 1] * remainder
    
    return result
