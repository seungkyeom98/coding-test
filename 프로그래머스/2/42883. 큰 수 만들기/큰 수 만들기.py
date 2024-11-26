def solution(number, k):
    stack = []  # 최종 결과를 저장할 스택
    
    for digit in number:
        # 스택이 비어 있지 않고, 제거할 수 있는 기회가 남아 있으며
        # 스택의 마지막 값이 현재 숫자보다 작으면 제거
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        
        # 현재 숫자를 스택에 추가
        stack.append(digit)
    
    # 제거 횟수가 남아 있으면 뒤에서 자른다
    if k > 0:
        stack = stack[:-k]
    
    # 스택에 있는 숫자를 합쳐서 결과 반환
    return ''.join(stack)