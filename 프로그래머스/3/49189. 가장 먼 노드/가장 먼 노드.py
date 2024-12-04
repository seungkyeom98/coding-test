from collections import deque, defaultdict

def solution(n, vertex):
    # 그래프를 인접 리스트로 표현
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS를 위한 준비
    distances = [-1] * (n + 1)  # 모든 노드의 거리를 -1로 초기화
    distances[1] = 0  # 1번 노드의 거리는 0
    queue = deque([1])  # BFS 큐 초기화
    
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == -1:  # 방문하지 않은 노드만 처리
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
    
    # 최장 거리와 해당 거리의 노드 개수 계산
    max_distance = max(distances)
    return distances.count(max_distance)