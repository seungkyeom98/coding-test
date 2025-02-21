def solution(order):
    stack = []
    count = 0
    index = 0  # order 리스트의 순서를 따라가기 위한 변수
    n = len(order)  # 상자의 개수
    
    for i in range(1, n + 1):  # 1번 상자부터 n번 상자까지 확인
        if i == order[index]:  # 바로 트럭에 적재 가능하면 적재
            count += 1
            index += 1
            # 보조 컨테이너 벨트(stack)의 top이 order[index]와 같다면 계속 pop
            while stack and stack[-1] == order[index]:
                stack.pop()
                count += 1
                index += 1
        else:
            stack.append(i)  # 보조 컨테이너 벨트에 보관

    return count
