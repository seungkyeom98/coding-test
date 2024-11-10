def solution(n):
    answer = 0
    fibo=[0,1]
    # fibo[0]=0
    # fibo[1]=1
    # fibo[2]=1
    # fibo[3]=2
    # fibo[4]=3
    # fibo[5]=5
    # fibo[6]=8
    # fibo[7]=13
    i=2
    while True:
        fibo.append(fibo[i-1]+fibo[i-2])
        i+=1
        if len(fibo)==(n+1):
            # fIndex=fibo.index(n)
            answer= (fibo[n-1]+fibo[n-2])%1234567
            break
        
        
    return answer

# def solution(n):
#     fibo = [0, 1]
    
#     for i in range(2, n + 1):
#         next_fibo = (fibo[i - 1] + fibo[i - 2]) % 1234567
#         fibo.append(next_fibo)
    
#     return fibo[n]