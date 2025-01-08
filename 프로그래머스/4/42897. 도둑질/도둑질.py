def solution(money):
    n = len(money)
    if n == 3:
        return max(money)  # 집이 3개라면, 인접하지 않은 하나의 집을 선택
    
    # 첫 번째 집을 포함하고 마지막 집 제외
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, n-1):  # 마지막 집 제외
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫 번째 집 제외하고 마지막 집 포함
    dp2 = [0] * n
    dp2[1] = money[1]
    for i in range(2, n):  # 첫 번째 집 제외
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[n-2], dp2[n-1])
