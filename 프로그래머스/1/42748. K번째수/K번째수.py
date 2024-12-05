def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        # 배열을 i번째부터 j번째까지 자르고 정렬
        sliced_sorted = sorted(array[i-1:j])
        # k번째 숫자를 결과에 추가 (k는 1-based index)
        result.append(sliced_sorted[k-1])
    return result