def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 마지막 요소 제거
        else:
            stack.append(char)  # 스택에 추가

    return 1 if not stack else 0

    
    

    return answer