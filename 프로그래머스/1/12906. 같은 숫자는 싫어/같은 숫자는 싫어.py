def solution(arr):
    # 결과를 저장할 리스트
    result = []
    
    # 배열을 순회하며 연속적인 중복 제거
    for i in range(len(arr)):
        # 첫 원소이거나 이전 원소와 다를 때만 추가
        if i == 0 or arr[i] != arr[i-1]:
            result.append(arr[i])
    
    return result