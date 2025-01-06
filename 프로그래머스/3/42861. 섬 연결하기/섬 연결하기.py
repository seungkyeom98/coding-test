def solution(n, costs):
    # 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])
    
    # Union-Find를 위한 부모 배열 초기화
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootY] = rootX
    
    # 최소 비용 계산
    total_cost = 0
    for a, b, cost in costs:
        if find(a) != find(b):  # 사이클이 생기지 않을 때만 추가
            union(a, b)
            total_cost += cost
    
    return total_cost
