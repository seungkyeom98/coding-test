from collections import deque

def solution(maps):
    # 상, 하, 좌, 우로 이동하는 방향 벡터 설정
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 맵의 크기
    n, m = len(maps), len(maps[0])
    
    # BFS를 위한 큐 설정
    queue = deque([(0, 0, 1)])  # (행, 열, 이동 거리)
    visited = [[False] * m for _ in range(n)]  # 방문 여부 체크
    visited[0][0] = True  # 시작점 방문 처리
    
    while queue:
        x, y, distance = queue.popleft()
        
        # 상대 팀 진영에 도착했을 때, 이동 거리 반환
        if x == n - 1 and y == m - 1:
            return distance
        
        # 4방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 맵 범위를 벗어나지 않고, 이동할 수 있는 칸(1)이며, 방문하지 않은 곳이라면
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny, distance + 1))  # 이동 거리 + 1로 큐에 추가
    
    # 상대 팀 진영에 도착할 수 없는 경우
    return -1