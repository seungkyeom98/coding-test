def solution(numbers):
    n = len(numbers)
    answer = [-1] * n  # 기본값 -1로 초기화
    stack = []  # 스택에는 numbers의 인덱스를 저장

    for i in range(n):
        # 스택이 비어 있지 않고, 현재 numbers[i]가 스택 top보다 크다면 갱신
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)  # 현재 인덱스를 스택에 추가

    return answer
