from collections import defaultdict, deque

def solution(n, wires):
    def bfs(start, graph, visited):
        queue = deque([start])
        visited[start] = True
        count = 1  # 시작 노드 포함
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count

    # 그래프 생성
    graph = defaultdict(list)
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_difference = float('inf')

    # 각 전선을 하나씩 제거하며 탐색
    for v1, v2 in wires:
        # 그래프에서 전선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        # 두 컴포넌트의 크기 계산
        visited = [False] * (n + 1)
        count1 = bfs(1, graph, visited)
        count2 = n - count1

        # 차이 계산 및 최소값 갱신
        min_difference = min(min_difference, abs(count1 - count2))

        # 그래프 복구
        graph[v1].append(v2)
        graph[v2].append(v1)

    return min_difference