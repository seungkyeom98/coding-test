def solution(s):
    # 문자열을 공백 기준으로 분리하여 정수형 리스트로 변환
    numList = list(map(int, s.split()))
    # 문자열.split() 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수
    
    # 최소값과 최대값을 찾아 문자열 형식으로 반환
    answer = f"{min(numList)} {max(numList)}"
    return answer