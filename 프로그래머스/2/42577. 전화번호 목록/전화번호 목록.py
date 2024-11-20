def solution(phone_book):
    phone_book.sort()  # 정렬, 숫자 문자열은 첫글자 숫자부터 순서대로 정렬됨.
    for i in range(len(phone_book) - 1): #i+1를 조사하기 때문에 len()에서 -1해야, 마지막 인덱스-1까지for문이 돌아간다.
        if phone_book[i+1].startswith(phone_book[i]):  # i인덱스 원소가 i+1인덱스 원소의 접두어인지 확인하는 메소드.
            return False
    return True