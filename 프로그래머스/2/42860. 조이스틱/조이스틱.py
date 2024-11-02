def solution(name):
    answer = 0
    
    # 상하 이동 횟수 계산
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        # ord('문자'): 문자를 유니코드에 맞는 숫자로 return해줌.
        # a~z는 97~122, A~Z는 60~95임 유니코드.(참고: 유니코드는 알파벳이나 한글의 한문자를 1대1 매칭이라 'ZZ' 또는 '키링' 이렇게 두글자는 대칭되는 유니코드 없으니, 그런건 ord()함수에 넣지마라. 한글자만 1대1대칭되는 유니코드 있으므로, ord()함수엔 한글자씩 넣어서 매칭되는 유니코드 찾으셈 ㅇㅇ)
        # min으로 둘중 최소값을 return함.
        # ord('Z') - ord(char) + 1는 'A'시작에서 'Z'로 한번 움직인 걸 +1 해준거임.
    
    # 좌우 이동 횟수 계산
    minMove = len(name) - 1  # 3글자면 2번만 움직임. 4글자면 3번 움직임.
    
    for i in range(len(name)):
        nextIndex = i + 1 # name문자열에서 다음글자 인덱스 번호
        
        # 다음글자가 'A'면 건너뛰고 그 다음 글자를 확인하기위해 nextIndex에 +1하는거임.
        # 'A'가 안오거나, nextIndex가 name의 인덱스 length와 같아지면 while끝.(같거나 넘으면 이라고 해도됨)
        # 반대로 while이 계속하려면 방금 조건식을 반대로 씀.
        # ( name[nextIndex] != 'A' or nextIndex >=len(name) )'
        # nextIndex < len(name) and name[nextIndex] == 'A' #드로므간 법칙
        while nextIndex < len(name) and name[nextIndex] == 'A':
            nextIndex += 1 
            
        # 좌우 이동의 최소 이동
        move_forward_and_back = i * 2 + (len(name) - nextIndex)
        # "BBAAAABBB"이면 오른쪽으로 갔다가 돌아가는게 이득임, 중간 A들 건들 필요없이 
        # 오른쪽으로 1번 가서 B쓰고, 다시 왼쪽으로 4번 가서 차례대로 끝쪽 B쓰면 총 5번만 움직이면 됨.
        # (근데 왼쪽 갔다가 오른쪽으로 가면, 왼쪽 3번, 오른쪽 4번, 총 7번임.)
        # (계속 오른쪽으로 쭉 갔다면, 8번 가야 맨 끝 끝쪽 B쓸 수 있음)
        # (오른쪽으로 쭉가는 건 맨처음 minMove에 저장해놓음. minMove= len(name) - 1로)
        move_backward_then_forward = i + (len(name) - nextIndex) * 2
        # "BBBAAAB"이면 뒤로 돌아서 왼쪽으로 먼저갔다가 오른쪽으로 가는게 빠름.
        # 왼쪽으로 먼저 가면 왼쪽 1번, 오른쪽 3번, 총 4번임
        # (근데 오른쪽 갔다가 왼쪽 뒤로 돌아가면, 오른쪽 2번 왼쪽 3번, 총 5번임.)        
        distance = min(move_forward_and_back, move_backward_then_forward)
        
        minMove = min(minMove, distance)
    
    answer += minMove
    return answer