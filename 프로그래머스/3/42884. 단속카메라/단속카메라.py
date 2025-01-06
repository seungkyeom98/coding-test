def solution(routes):
    # 1. 경로를 종료 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    
    # 2. 카메라 설치
    cameras = []
    count = 0
    last_camera = -30001  # 카메라가 설치된 마지막 위치 (초기값은 범위 밖)
    
    for route in routes:
        start, end = route
        # 카메라가 현재 차량의 경로를 커버하지 못하는 경우
        if last_camera < start:
            count += 1
            last_camera = end  # 새로운 카메라 설치
    
    return count
