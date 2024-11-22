from collections import Counter

#collections.Counter는 데이터의 요소를 카운트하여 빈도수를 저장하는 딕셔너리와 유사한 객체
#키는 요소, 값은 해당 요소의 빈도수
#Counter 객체끼리 덧셈, 뺄셈, 교집합, 합집합 연산이 가능

def solution(participant, completion):
    #print(Counter(participant), list(Counter(participant))) 
    # 출력해보면, 자료형이 달라서, 출력결과가 다르다.
    return list(Counter(participant) - Counter(completion))[0] #리스트 형식으로 반환해야, 정답이라 인식함