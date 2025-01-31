from itertools import permutations
import re

def is_match(user, banned):
    """정규 표현식을 이용해 user_id가 banned_id 패턴과 일치하는지 확인"""
    pattern = "^" + banned.replace('*', '.') + "$"
    return re.match(pattern, user) is not None

def solution(user_id, banned_id):
    possible_sets = set()
    
    # 응모자 아이디 중에서 불량 사용자 패턴과 일치하는 조합을 찾음
    for candidate in permutations(user_id, len(banned_id)):
        if all(is_match(u, b) for u, b in zip(candidate, banned_id)):
            possible_sets.add(frozenset(candidate))  # 순서가 다르더라도 같은 조합이면 하나로 처리하기 위해 frozenset 사용

    return len(possible_sets)
