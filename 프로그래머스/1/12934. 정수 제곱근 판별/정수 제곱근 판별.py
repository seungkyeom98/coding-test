def solution(n):
    # n의 제곱근을 구합니다.
    sqrt_n = int(n ** 0.5)
    
    # n이 완전제곱수인지 확인합니다.
    if sqrt_n * sqrt_n == n:
        # 완전제곱수라면 (x+1)의 제곱을 반환합니다.
        return (sqrt_n + 1) ** 2
    else:
        # 완전제곱수가 아니라면 -1을 반환합니다.
        return -1