def solution(n):
    answer = n
    for i in range(1,n+1):
        if n%i==1 and i<answer:
            answer=i
            
    return answer