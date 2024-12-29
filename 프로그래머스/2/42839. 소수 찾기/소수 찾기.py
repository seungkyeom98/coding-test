from itertools import permutations

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    # 모든 숫자 조합 생성
    number_combinations = set()
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for p in perms:
            number = int("".join(p))
            number_combinations.add(number)
    
    # 소수 판별
    prime_count = 0
    for num in number_combinations:
        if is_prime(num):
            prime_count += 1
    
    return prime_count
