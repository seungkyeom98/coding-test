def solution(triangle):
    # 삼각형의 높이
    n = len(triangle)
    
    # 동적 프로그래밍을 위한 2차원 배열 생성
    dp = [row[:] for row in triangle]  # 원본 삼각형을 복사하여 사용

    # dp 배열 업데이트
    for i in range(1, n):  # 첫 번째 줄은 그대로 사용
        for j in range(i + 1):
            if j == 0:  # 맨 왼쪽
                dp[i][j] += dp[i - 1][j]
            elif j == i:  # 맨 오른쪽
                dp[i][j] += dp[i - 1][j - 1]
            else:  # 중간
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    # 마지막 줄의 최댓값 반환
    return max(dp[-1])