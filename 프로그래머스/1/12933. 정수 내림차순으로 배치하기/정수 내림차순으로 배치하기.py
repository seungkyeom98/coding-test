def solution(n):
    answer = 0
    list1 = list(str(n))
    list1.sort(reverse=1)
    answer = int(''.join(list1))
    return answer