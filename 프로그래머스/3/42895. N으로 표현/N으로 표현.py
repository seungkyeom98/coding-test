def solution(N, number):
    if N == number:  # N과 number가 같으면 N을 한 번만 사용
        return 1

    # 동적 프로그래밍을 위한 리스트 초기화
    dp = [set() for _ in range(9)]  # dp[i]는 N을 i번 사용해서 만들 수 있는 값의 집합

    # N을 i번 반복해서 만든 값을 추가
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN, ...
                                    #set자료형은 add메소드로 원소를 추가한다.
        
    # 사칙연산으로 가능한 값들을 계산
    for i in range(1, 9):  # i는 현재 사용하는 N의 개수
        for j in range(1, i):  # j와 i-j로 나누어 계산
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)  # 덧셈
                    dp[i].add(x - y)  # 뺄셈
                    dp[i].add(x * y)  # 곱셈
                    if y != 0:  # 나눗셈 (0으로 나누기 방지)
                        dp[i].add(x // y)

        # 현재 단계에서 number가 생성되었다면 반환
        if number in dp[i]:
            return i

    # 8번 반복 후에도 찾지 못하면 -1 반환
    return -1