def solution(arr1, arr2):
    row1, col1 = len(arr1), len(arr1[0])
    row2, col2 = len(arr2), len(arr2[0])
    
    # 결과 행렬 초기화 (row1 x col2 크기의 행렬)
    result = [[0] * col2 for _ in range(row1)]
    
    # 행렬 곱셈 수행
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):  # 또는 row2 (col1 == row2 이므로)
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result
