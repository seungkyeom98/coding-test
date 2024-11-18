def solution(n, words):
    used_words = set()  # 이미 말한 단어를 저장
    last_word = ""  # 이전 단어의 마지막 글자를 추적
    
    for i, word in enumerate(words):
        # 규칙 위반 검사
        # last_word가 비어 있지 않을 때(즉, 게임이 처음 시작이 아닌 경우)에만 뒤의 조건을 검사
        # if 조건식에 last_word가 같이 문자열만 딸랑 들어가있으면, 빈 문자열 ""이면, False.
        # 문자열 안에 한글자라도 있으면, True.
        # last_word가 빈 문자열 ""이면 False로 and뒤에 last_word[-1] !=word[0]조건을 볼필요없이 False됨.
        if (word in used_words) or (last_word and last_word[-1] != word[0]) or len(word) < 2:
            # 탈락자 번호와 차례 계산
            player = (i % n) + 1  # 현재 플레이어 번호,  n으로 나눠야 2바퀴 3바퀴째도 현재 플레이어 번호 알수있음.
            turn = (i // n) + 1  # 현재 차례, 1바퀴째, 2바퀴째인지를 의미.
            return [player, turn]
        
        # 단어를 사용 처리
        used_words.add(word) # set자료형.add메소드는 문자열을 분리하지 않고 저장. 
                             # set자료형.update메소드는 문자열을 분리해서 저장. 
        last_word = word  # 현재 단어를 이전 단어로 설정
    
    return [0, 0]  # 규칙 위반이 없으면 [0, 0] 반환