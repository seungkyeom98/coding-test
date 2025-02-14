def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 길이 반환

    max_length = 0
    for i in range(len(s)):
        max_length = max(max_length, expand(i, i), expand(i, i + 1))

    return max_length
