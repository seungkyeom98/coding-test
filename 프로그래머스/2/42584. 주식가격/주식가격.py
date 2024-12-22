def solution(prices):
    n = len(prices)
    answer = [0] * n  # 각 가격이 유지된 시간을 저장할 배열
    stack = []  # 스택에는 가격이 떨어지지 않은 시점의 인덱스를 저장

    for i in range(n):
        # 스택에 저장된 시점들 중 현재 가격보다 높은 시점들을 제거하며 시간 계산
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top  # 가격이 유지된 시간 계산
        stack.append(i)  # 현재 시점 인덱스를 스택에 추가

    # 스택에 남아있는 인덱스들은 끝까지 가격이 떨어지지 않았던 시점들
    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer