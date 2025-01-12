from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 2배 확장
    MAX = 102
    field = [[0] * MAX for _ in range(MAX)]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x == x1 or x == x2 or y == y1 or y == y2:  # 테두리
                    if field[x][y] != 2:  # 내부가 아닌 경우
                        field[x][y] = 1
                else:  # 내부
                    field[x][y] = 2

    # BFS 탐색
    def bfs(start, end):
        visited = [[False] * MAX for _ in range(MAX)]
        queue = deque([start])
        visited[start[0]][start[1]] = True
        distance = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == end:
                    return distance // 2  # 확장한 좌표이므로 다시 축소
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < MAX and 0 <= ny < MAX and not visited[nx][ny] and field[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            distance += 1
    
    # 좌표 확장
    start = (characterX * 2, characterY * 2)
    end = (itemX * 2, itemY * 2)
    
    return bfs(start, end)
