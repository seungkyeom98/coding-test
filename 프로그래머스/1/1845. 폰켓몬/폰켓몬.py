def solution(nums):
    answer = len(set(nums))  # 중복 제거 후 가져갈 최대 종류 개수
    if answer > len(nums)/2:  # 가져갈 수 있는 최대 마리 수
            answer = len(nums)/2
    return answer