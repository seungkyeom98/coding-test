import heapq

def solution(jobs):
    # 작업을 요청 시점 기준으로 정렬
    jobs.sort()
    current_time = 0  # 현재 시각
    total_turnaround_time = 0  # 총 반환 시간
    waiting_queue = []  # 대기 큐
    idx = 0  # jobs 리스트의 인덱스
    job_count = len(jobs)  # 총 작업 수

    while idx < job_count or waiting_queue:
        # 현재 시간까지 도착한 작업들을 대기 큐에 추가
        while idx < job_count and jobs[idx][0] <= current_time:
            request_time, duration = jobs[idx]
            heapq.heappush(waiting_queue, (duration, request_time))
            idx += 1

        if waiting_queue:
            # 대기 큐에서 가장 소요 시간이 짧은 작업을 꺼냄
            duration, request_time = heapq.heappop(waiting_queue)
            current_time += duration
            total_turnaround_time += current_time - request_time
        else:
            # 대기 큐가 비어 있으면 다음 작업의 요청 시점으로 이동
            current_time = jobs[idx][0]

    # 평균 반환 시간의 정수 부분을 반환
    return total_turnaround_time // job_count
