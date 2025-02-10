from collections import defaultdict

def solution(gems):
    gem_types = len(set(gems))  # 보석 종류 개수
    gem_count = defaultdict(int)  # 현재 구간의 보석 개수 저장
    min_range = [0, len(gems)]  # 최소 구간 초기화
    left = 0  # 왼쪽 포인터
    right = 0  # 오른쪽 포인터
    gem_count[gems[0]] = 1  # 첫 번째 보석 추가

    while right < len(gems):
        # 현재 구간이 모든 보석을 포함하는 경우
        if len(gem_count) == gem_types:
            # 최소 길이 구간 갱신
            if (right - left) < (min_range[1] - min_range[0]):
                min_range = [left, right]

            # 왼쪽 포인터 이동 (구간을 줄여서 더 작은 범위 찾기)
            gem_count[gems[left]] -= 1
            if gem_count[gems[left]] == 0:  # 보석 개수가 0이 되면 제거
                del gem_count[gems[left]]
            left += 1

        # 현재 구간이 모든 보석을 포함하지 못한 경우, 오른쪽 포인터 확장
        else:
            right += 1
            if right < len(gems):  # 범위 체크 후 보석 추가
                gem_count[gems[right]] += 1

    # 최종 구간의 시작점과 끝점 (1-based index로 변환)
    return [min_range[0] + 1, min_range[1] + 1]
