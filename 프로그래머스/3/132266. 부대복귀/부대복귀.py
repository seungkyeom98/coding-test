from collections import deque

def solution(n, roads, sources, destination):
    # 그래프 생성
    graph = {i: [] for i in range(1, n+1)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS로 최단 거리 계산
    distances = {i: -1 for i in range(1, n+1)}  # 기본값 -1 (도달 불가)
    queue = deque([destination])
    distances[destination] = 0  # 목적지에서 목적지까지의 거리는 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 아직 방문하지 않은 경우
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    # sources에 대한 결과 반환
    return [distances[source] for source in sources]
