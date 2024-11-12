def solution(brown, yellow):
    total = brown + yellow  # 전체 격자 수
    
    for height in range(3, int(total**0.5) + 1):  # 세로 길이 (3 이상부터 시작)
        if total % height == 0:  # 나누어 떨어지는 가로 길이
            width = total // height
            # 조건 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]