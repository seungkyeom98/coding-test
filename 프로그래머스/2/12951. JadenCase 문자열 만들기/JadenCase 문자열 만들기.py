def solution(s):
    answer = ''
    li1= s.split(" ") # 공백을 포함하여 단어를 나눔
    temp = ''
    print(li1)
    for i in range(len(li1)):
        if li1[i]: #단어가 비어있지 않은 경우에만 처리
            li1[i]=li1[i].capitalize()

    answer= " ".join(li1)
    print(li1)
    
    
    
    
    return answer