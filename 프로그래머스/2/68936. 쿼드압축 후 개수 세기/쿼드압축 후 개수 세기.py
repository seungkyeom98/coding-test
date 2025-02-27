def solution(arr):
    def compress(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:  # 값이 다르면 분할 수행
                    half = size // 2
                    compress(x, y, half)
                    compress(x, y + half, half)
                    compress(x + half, y, half)
                    compress(x + half, y + half, half)
                    return
        # 모든 값이 동일하면 개수 추가
        counts[first] += 1

    counts = [0, 0]  # 0의 개수, 1의 개수
    compress(0, 0, len(arr))
    return counts
