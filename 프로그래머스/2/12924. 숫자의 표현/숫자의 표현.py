def solution(n):
    count = 0
    
    for i in range(1, n + 1):
        num = 0
        for j in range(i, n + 1):
            num += j
            if num == n:
                count += 1
                break
            elif num > n:
                break
                
    return count