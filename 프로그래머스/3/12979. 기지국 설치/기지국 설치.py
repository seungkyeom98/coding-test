import math

def solution(N, stations, W):
    answer = 0
    coverage = 2 * W + 1  # 한 개의 기지국이 커버할 수 있는 범위

    # 1. 기존 기지국이 커버하지 못하는 영역을 찾는다.
    uncovered_zones = []
    
    # 첫 번째 기지국 앞에 커버되지 않는 영역
    if stations[0] - W > 1:
        uncovered_zones.append((1, stations[0] - W - 1))
    
    # 기지국 사이의 커버되지 않는 영역
    for i in range(len(stations) - 1):
        prev_station_end = stations[i] + W
        next_station_start = stations[i+1] - W
        if prev_station_end + 1 < next_station_start:
            uncovered_zones.append((prev_station_end + 1, next_station_start - 1))

    # 마지막 기지국 뒤에 커버되지 않는 영역
    if stations[-1] + W < N:
        uncovered_zones.append((stations[-1] + W + 1, N))

    # 2. 커버되지 않는 영역을 최소 기지국으로 커버
    for start, end in uncovered_zones:
        length = end - start + 1
        answer += math.ceil(length / coverage)

    return answer
