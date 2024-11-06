def solution(s):

    count =0
    num=0
    
    while s != '1':
        num+=s.count('0')
        s= s.replace('0','')
        s= bin(len(s))[2:] #0b 접두어 제거
        count+=1
        
    answer = [count,num]
    return answer