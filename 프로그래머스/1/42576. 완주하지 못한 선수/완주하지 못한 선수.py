from collections import Counter

#collections.Counter는 데이터의 요소를 카운트하여 빈도수를 저장하는 딕셔너리와 유사한 객체
#키는 요소, 값은 해당 요소의 빈도수
#Counter 객체끼리 덧셈, 뺄셈, 교집합, 합집합 연산이 가능

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]