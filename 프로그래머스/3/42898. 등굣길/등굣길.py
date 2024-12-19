def solution(m, n, puddles):
    # 경로 수를 저장할 2차원 배열 초기화
    dp = [[0] * m for _ in range(n)]
    
    # 시작점 초기화
    dp[0][0] = 1
    
    # 물에 잠긴 지역을 표시할 집합
    puddle_set = {(y - 1, x - 1) for x, y in puddles}
    
    for i in range(n):
        for j in range(m):
            # 시작점이거나 물에 잠긴 지역인 경우 처리
            if (i, j) == (0, 0) or (i, j) in puddle_set:
                continue
            # 왼쪽에서 오는 경로와 위쪽에서 오는 경로를 합산
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
            # 결과를 모듈러 연산
            dp[i][j] %= 1_000_000_007

    return dp[n - 1][m - 1]