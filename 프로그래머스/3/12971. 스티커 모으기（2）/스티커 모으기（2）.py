def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    def get_max(stickers):
        n = len(stickers)
        if n == 1:
            return stickers[0]
        if n == 2:
            return max(stickers[0], stickers[1])

        dp = [0] * n
        dp[0] = stickers[0]
        dp[1] = max(stickers[0], stickers[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + stickers[i])

        return dp[-1]

    # 첫 번째 스티커를 선택하는 경우 (마지막 스티커는 제외)
    case1 = get_max(sticker[:-1])
    # 첫 번째 스티커를 선택하지 않는 경우 (첫 번째 스티커는 제외)
    case2 = get_max(sticker[1:])

    return max(case1, case2)
