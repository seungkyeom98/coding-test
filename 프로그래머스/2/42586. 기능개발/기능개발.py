import math

def solution(progresses, speeds):
    answer = []
    # 작업 별로 필요한 완료 일수 계산
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    # 배포 작업 수 계산
    current = days[0]  # 첫 작업의 완료 예정일
    count = 0          # 배포할 작업의 수

    for day in days:
        if day <= current:
            # 현재 작업이 현재 배포 기준일 이내에 완료된다면 count 증가
            count += 1
        else:
            # 새로운 배포 필요
            answer.append(count)
            current = day
            count = 1
    answer.append(count)  # 마지막 배포 묶음 추가
    
    return answer