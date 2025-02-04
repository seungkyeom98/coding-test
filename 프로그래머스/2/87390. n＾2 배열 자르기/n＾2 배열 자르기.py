def solution(n, left, right):
    result = [(max(i // n, i % n) + 1) for i in range(left, right + 1)]
    return result
