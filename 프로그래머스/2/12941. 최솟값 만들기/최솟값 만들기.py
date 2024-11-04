def multiply(a,b):
    return a*b
def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)

    # answer = list(map(multiply,A,B))
    answer = map(multiply,A,B)
    # print(answer)
    # print(sum(answer))

    return sum(answer)