def solution(sequence):
    n = len(sequence)
    
    # 두 가지 펄스 수열 생성
    pulse1 = [1 if i % 2 == 0 else -1 for i in range(n)]
    pulse2 = [-1 if i % 2 == 0 else 1 for i in range(n)]
    
    # 펄스를 적용한 두 개의 새로운 수열
    seq1 = [sequence[i] * pulse1[i] for i in range(n)]
    seq2 = [sequence[i] * pulse2[i] for i in range(n)]
    
    # Kadane's Algorithm으로 최대 부분합 계산
    def max_subarray_sum(arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    return max(max_subarray_sum(seq1), max_subarray_sum(seq2))
