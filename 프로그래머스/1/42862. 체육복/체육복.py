def solution(n, lost, reserve):
    
    realLost = set(lost)- set(reserve)
    realReserve = set(reserve)-set(lost)
    answer = n-len(realLost)
    for i in realReserve:
        if i-1 in realLost:
            realLost.remove(i-1)
            answer+=1 
        elif i+1 in realLost:
            realLost.remove(i+1)
            answer+=1

                
    
    
    
    return answer