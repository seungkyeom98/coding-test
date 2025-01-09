from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def can_transform(word1, word2):
        # 두 단어가 한 글자만 다른지 확인
        diff_count = sum([1 for a, b in zip(word1, word2) if a != b])
        return diff_count == 1

    # BFS를 위한 큐 초기화
    queue = deque([(begin, 0)])  # (현재 단어, 변환 단계)
    visited = set()  # 방문한 단어 기록

    while queue:
        current_word, steps = queue.popleft()

        # 현재 단어가 목표 단어인지 확인
        if current_word == target:
            return steps

        # 방문하지 않은 단어 중 변환 가능한 단어 찾기
        for word in words:
            if word not in visited and can_transform(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0
