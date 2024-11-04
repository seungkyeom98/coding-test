def solution(s):
    answer = True
    
    # 첫 번째 괄호가 '('인지 확인
    if s[0] == '(':
        count = 0  # 여는 괄호와 닫는 괄호의 균형을 맞추기 위한 카운터
        
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
            
            # 닫는 괄호가 여는 괄호보다 많아지면 올바르지 않음
            if count < 0:
                answer = False
                break

        # 최종적으로 여는 괄호와 닫는 괄호가 같아야 함
        if count != 0:
            answer = False
    else:
        answer = False

    return answer