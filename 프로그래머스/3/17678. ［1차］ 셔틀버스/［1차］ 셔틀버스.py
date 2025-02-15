from datetime import datetime, timedelta

def to_minutes(time_str):
    """ HH:MM 형식을 분(minute)으로 변환 """
    h, m = map(int, time_str.split(":"))
    return h * 60 + m

def to_time_str(minutes):
    """ 분(minute)을 HH:MM 형식으로 변환 """
    return f"{minutes // 60:02}:{minutes % 60:02}"

def solution(n, t, m, timetable):
    # 크루 도착 시간 정렬 (분 단위 변환)
    crew_times = sorted(to_minutes(time) for time in timetable)
    
    # 셔틀 도착 시간 리스트 (09:00부터 t분 간격으로 n회)
    shuttle_times = [to_minutes("09:00") + i * t for i in range(n)]
    
    crew_index = 0  # 대기 중인 크루의 인덱스
    
    for shuttle in shuttle_times:
        # 현재 셔틀에 탑승할 크루 리스트 (최대 m명)
        passengers = []
        
        while crew_index < len(crew_times) and len(passengers) < m and crew_times[crew_index] <= shuttle:
            passengers.append(crew_times[crew_index])
            crew_index += 1
        
        # 마지막 셔틀이면 콘이 탈 시간 결정
        if shuttle == shuttle_times[-1]:
            if len(passengers) < m:  
                # 자리가 남아 있으면 콘은 셔틀 도착 시간에 맞춰 도착
                return to_time_str(shuttle)
            else:
                # 자리가 꽉 찼다면 마지막으로 탄 크루보다 1분 먼저 도착
                return to_time_str(passengers[-1] - 1)
