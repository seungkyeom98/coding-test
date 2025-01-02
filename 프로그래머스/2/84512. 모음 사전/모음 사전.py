def solution(word):
    # 각 자리의 가중치 계산
    weights = [781, 156, 31, 6, 1]  # (5^4 + 5^3 + 5^2 + 5^1 + 1) 순으로 계산됨
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    # 순서 계산
    result = 0
    for i, char in enumerate(word):
        # 해당 문자가 모음 리스트에서 몇 번째인지 찾기
        index = vowels.index(char)
        # 가중치 곱하여 순서 계산
        result += index * weights[i] + 1
    
    return result
