from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (현재값, 인덱스)를 원소로 가지는 2차원 리스트. 큐.
    count = 0
    
    while queue:
        current_sum, index = queue.popleft() #선입 선출후, 그 값을 return.
        
        if index == len(numbers):
            if current_sum == target:
                count += 1
        else:
            queue.append((current_sum + numbers[index], index + 1))
            queue.append((current_sum - numbers[index], index + 1))
    
    return count