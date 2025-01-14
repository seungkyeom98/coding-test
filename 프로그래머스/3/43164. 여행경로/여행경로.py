from collections import defaultdict

def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    # 목적지를 알파벳 순서로 정렬
    for key in graph:
        graph[key].sort(reverse=True)  # 역순으로 정렬하여 pop() 사용

    stack = ["ICN"]
    path = []

    while stack:
        current = stack[-1]
        # 더 이상 방문할 경로가 없는 경우
        if current not in graph or len(graph[current]) == 0:
            path.append(stack.pop())
        else:
            # 다음 목적지로 이동
            stack.append(graph[current].pop())
    
    # 역순으로 저장되었으므로 뒤집어서 반환
    return path[::-1]
