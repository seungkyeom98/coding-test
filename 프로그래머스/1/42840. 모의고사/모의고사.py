def solution(answers):
    # 1번, 2번, 3번 수포자의 찍는 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 정답을 맞힌 개수를 저장하는 리스트
    scores = [0, 0, 0]
    
    # 각 수포자의 점수를 계산
    for i, answer in enumerate(answers):
        if answer == pattern1[i % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[i % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[i % len(pattern3)]:
            scores[2] += 1
    
    # 가장 높은 점수 찾기
    max_score = max(scores)
    
    # 가장 높은 점수를 받은 수포자 반환 (오름차순 정렬)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    return result