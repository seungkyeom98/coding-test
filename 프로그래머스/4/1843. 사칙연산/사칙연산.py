def solution(arr):
    def calculate(a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b

    n = len(arr)
    dp_max = [[-float('inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    # 숫자 초기화
    for i in range(0, n, 2):  # 숫자 위치는 항상 짝수 인덱스
        dp_max[i][i] = dp_min[i][i] = int(arr[i])

    # 구간 길이 증가
    for length in range(3, n + 1, 2):  # 구간 길이는 항상 홀수 (숫자 + 연산자)
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):  # 연산자 위치
                op = arr[k]
                dp_max[i][j] = max(
                    dp_max[i][j],
                    calculate(dp_max[i][k - 1], dp_max[k + 1][j], op),
                    calculate(dp_max[i][k - 1], dp_min[k + 1][j], op),
                    calculate(dp_min[i][k - 1], dp_max[k + 1][j], op),
                    calculate(dp_min[i][k - 1], dp_min[k + 1][j], op),
                )
                dp_min[i][j] = min(
                    dp_min[i][j],
                    calculate(dp_max[i][k - 1], dp_max[k + 1][j], op),
                    calculate(dp_max[i][k - 1], dp_min[k + 1][j], op),
                    calculate(dp_min[i][k - 1], dp_max[k + 1][j], op),
                    calculate(dp_min[i][k - 1], dp_min[k + 1][j], op),
                )

    return dp_max[0][n - 1]
