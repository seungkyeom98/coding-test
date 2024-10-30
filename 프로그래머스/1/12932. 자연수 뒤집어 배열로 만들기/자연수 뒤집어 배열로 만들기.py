def solution(n):
    list1 = list(str(n))
    list1.reverse()
    answer = []
    for i in list1:
        answer.append(int(i))
    return answer