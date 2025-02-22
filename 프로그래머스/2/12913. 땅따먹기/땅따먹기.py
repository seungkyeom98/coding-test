def solution(land):
    for i in range(1, len(land)):  # 2번째 행부터 시작
        for j in range(4):  # 열 반복
            # 이전 행에서 같은 열을 제외한 최댓값을 현재 값과 더함
            land[i][j] += max(land[i-1][k] for k in range(4) if k != j)

    return max(land[-1])  # 마지막 행에서 최대값 반환
