from collections import deque

def solution(n, computers):
    def bfs(start, visited):
        # 큐 초기화
        queue = deque([start])
        visited[start] = True  # 시작 노드 방문 처리
        
        # 큐가 빌 때까지 탐색
        while queue:
            node = queue.popleft()  # 큐에서 하나를 꺼냄
            # 현재 노드에 연결된 노드를 탐색
            for connected_node in range(n):
                if computers[node][connected_node] == 1 and not visited[connected_node]:
                    visited[connected_node] = True  # 방문 처리
                    queue.append(connected_node)  # 큐에 추가

    visited = [False] * n  # 방문 여부 리스트
    network_count = 0  # 네트워크 개수

    # 모든 컴퓨터를 순회
    for i in range(n):
        if not visited[i]:  # 방문하지 않은 컴퓨터를 발견
            bfs(i, visited)  # 해당 컴퓨터를 기준으로 BFS 탐색
            network_count += 1  # 새로운 네트워크 발견

    return network_count