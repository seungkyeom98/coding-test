def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0: # 짝수이면
            n = n // 2 # 나누기 2
        else: # 홀수이면 
            n = n - 1 # 1칸 점프
            answer += 1 # 건전지 사용량 1추가
    
    return answer