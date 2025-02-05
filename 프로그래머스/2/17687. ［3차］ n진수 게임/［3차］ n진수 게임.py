def convert_to_base(n, num):
    """ 숫자 num을 n진수 문자열로 변환 """
    chars = "0123456789ABCDEF"
    result = ""
    
    if num == 0:
        return "0"

    while num > 0:
        result = chars[num % n] + result
        num //= n

    return result

def solution(n, t, m, p):
    full_sequence = ""
    num = 0
    
    # 필요한 만큼 숫자를 나열 (t * m 개)
    while len(full_sequence) < t * m:
        full_sequence += convert_to_base(n, num)
        num += 1

    # 튜브가 말해야 하는 숫자만 추출 (p번째 순서)
    return "".join(full_sequence[i] for i in range(p - 1, t * m, m))

# 예제 테스트
print(solution(2, 4, 2, 1))  # "0111"
print(solution(16, 16, 2, 1))  # "02468ACE11111111"
print(solution(16, 16, 2, 2))  # "13579BDF01234567"
