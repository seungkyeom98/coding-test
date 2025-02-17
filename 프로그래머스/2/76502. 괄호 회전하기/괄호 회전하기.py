def is_valid(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    
    return not stack  # 스택이 비어 있어야 올바른 괄호 문자열

def solution(s):
    count = 0
    n = len(s)
    
    for i in range(n):
        rotated = s[i:] + s[:i]  # 문자열 회전
        if is_valid(rotated):
            count += 1
            
    return count
