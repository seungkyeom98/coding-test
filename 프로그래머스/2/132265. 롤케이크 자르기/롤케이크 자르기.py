def solution(topping):
    from collections import defaultdict
    
    left_set = set()
    right_set = set()
    
    left_count = []
    right_count = [0] * len(topping)

    # 왼쪽에서 오른쪽으로 진행하며 철수의 토핑 종류 개수 저장
    for i in range(len(topping)):
        left_set.add(topping[i])
        left_count.append(len(left_set))
    
    # 오른쪽에서 왼쪽으로 진행하며 동생의 토핑 종류 개수 저장
    for i in range(len(topping) - 1, 0, -1):
        right_set.add(topping[i])
        right_count[i] = len(right_set)
    
    # 공평하게 나누는 경우의 수 계산
    answer = 0
    for i in range(len(topping) - 1):
        if left_count[i] == right_count[i + 1]:
            answer += 1
            
    return answer
