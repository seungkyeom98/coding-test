def solution(A, B):
    # 두 배열을 정렬
    A.sort()
    B.sort()

    # 투 포인터를 사용
    a_idx, b_idx = 0, 0  # A와 B의 인덱스
    score = 0  # B팀의 승점

    while b_idx < len(B):
        if B[b_idx] > A[a_idx]:  # B팀원이 A팀원을 이길 경우
            score += 1  # 승점 추가
            a_idx += 1  # A팀 다음 선수로 이동
        b_idx += 1  # B팀 다음 선수로 이동

    return score

# 테스트
A = [5, 1, 3, 7]
B = [2, 2, 6, 8]
solution(A, B)
