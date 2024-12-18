def solution(people, limit):
    people.sort()  # 몸무게를 오름차순으로 정렬
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람의 무게가 제한을 넘지 않는다면 같이 태운다
        if people[left] + people[right] <= limit:
            left += 1
        # 가장 무거운 사람은 항상 보트에 태워야 하므로 right를 감소
        right -= 1
        # 보트 사용 횟수 증가
        boats += 1
    
    return boats