import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville) #힙으로 변환
    mix_count = 0

    while len(scoville) > 1:
        # 가장 맵지 않은 두 개 추출
        least = heapq.heappop(scoville) #heapop쓰면,가장 작은 원소를 제거하고, 그 원소를 return함.
                                        #return된걸 least에 저장.
        if least >= K:      #가장작은 값이 K보다 크면, 섞는거 그만하고, mix_count return ㄱ.
            return mix_count
        second_least = heapq.heappop(scoville)#heapop으로 그다음 작은 원소 제거후, second_least에 저장
        
        # 섞은 음식 추가
        new_scoville = least + (second_least * 2)
        heapq.heappush(scoville, new_scoville)#원소값 오름차순으로 scoville리스트에 새로운값 추가
        mix_count += 1 #한번섞은거니, mix_count에 1추가
    
    # 음식 1개남았을때, while문 벗어나고, 그 값이 K를 넘는지 확인,
    # 안넘으면, -1 반환.
    if scoville[0] >= K:
        return mix_count
    else:
        return -1