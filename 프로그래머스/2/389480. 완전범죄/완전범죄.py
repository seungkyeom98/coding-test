def solution(info, n, m):
    # 최대 흔적 개수 설정 (최대 120)
    INF = float('inf')
    dp = [[[INF] * (m+1) for _ in range(n+1)] for _ in range(len(info) + 1)]
    
    # 초기 상태 (흔적 없음)
    dp[0][0][0] = 0  

    # DP 진행
    for i in range(len(info)):
        a_trace, b_trace = info[i]
        for a in range(n+1):
            for b in range(m+1):
                if dp[i][a][b] == INF:
                    continue
                
                # A도둑이 훔치는 경우
                if a + a_trace < n + 1:
                    dp[i+1][a + a_trace][b] = min(dp[i+1][a + a_trace][b], dp[i][a][b] + a_trace)
                
                # B도둑이 훔치는 경우
                if b + b_trace < m + 1:
                    dp[i+1][a][b + b_trace] = min(dp[i+1][a][b + b_trace], dp[i][a][b])
    # 정답 찾기
    result = INF
    for a in range(n):
        for b in range(m):
            result = min(result, dp[len(info)][a][b])
    return result if result != INF else -1
