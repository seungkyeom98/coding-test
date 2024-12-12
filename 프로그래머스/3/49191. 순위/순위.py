def solution(n, results):
    # 그래프 초기화
    graph = [[0] * n for _ in range(n)]
    
    # 주어진 결과 입력
    for win, lose in results:
        graph[win - 1][lose - 1] = 1  # 이김
        graph[lose - 1][win - 1] = -1  # 패배
    
    # 플로이드-워셜 알고리즘 적용
    for k in range(n):  # 중간 노드
        for i in range(n):  # 시작 노드
            for j in range(n):  # 도착 노드
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i가 j를 이김
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1  # i가 j에게 짐
    
    # 순위를 매길 수 있는 선수 계산
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != 0:  # 승패 관계가 명확하다면
                count += 1
        if count == n - 1:  # 다른 모든 선수와의 승패가 명확하면
            answer += 1
    
    return answer