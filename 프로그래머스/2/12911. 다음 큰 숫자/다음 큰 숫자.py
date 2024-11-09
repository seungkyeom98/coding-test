def solution(n):
    answer = 0
    i=1
    while True:
        bin1= bin(n) # 이진법 문자열임
        bin2= bin(n+i)
        if bin1.count('1')==bin2.count('1'):
            answer=int(bin2,2)
            break
        i+=1
    
    return answer