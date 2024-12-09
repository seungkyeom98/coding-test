def solution(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)
    # h-index 계산
    h_index = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index