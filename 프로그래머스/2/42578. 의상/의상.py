from collections import Counter
# counter가 리스트의 원소를 key로 하여, 빈도수를 value를 갖는 딕셔너리 형태의 iterable.
def solution(clothes):
    # 각 의상 종류별로 갯수 세기
    counter = Counter([kind for name, kind in clothes]) # 인자 풀기를 하고, kind만 리스트 컴프리핸션으로 저장
    
    # 조합 계산 (각 종류의 개수 + 1) 값을 곱함
    # 해당 의상을 입거나 입지 않는 경우가 있으므로, (의상 수 + 1)로 계산
    # 각 (종류+1)에 곱하기 ㄱ
    answer = 1
    for count in counter.values(): # 각 종류=key에 대한 빈도수를 count에 저장
        answer *= (count + 1)      # (각 종류의 개수 + 1)에 곱해서 저장
    
    # 최소 한 가지는 입어야 하므로, 아무것도 안 입는 경우(1)를 제외
    return answer - 1