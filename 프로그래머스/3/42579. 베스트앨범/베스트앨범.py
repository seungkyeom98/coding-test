from collections import defaultdict 

def solution(genres, plays):
    # 1. 장르별 총 재생 횟수와 곡 정보 저장
    genre_play_count = defaultdict(int)  # 장르별 총 재생 횟수
                        #해당하는 key가 없으면, 정수형 0으로 기본값(디폴트값)해서, 해당 키와 value생성!
    songs_by_genre = defaultdict(list)   # 장르별 곡 정보
                        #해당하는 key가 없으면, 리스트형 []으로 기본값(디폴트값)을 할당(=초기화)해서, 해당 키와 value생성!
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        genre_play_count[genre] += play
        songs_by_genre[genre].append((play, i))  # (재생 횟수, 고유 번호) 저장

    # 2. 장르별로 총 재생 횟수 내림차순 정렬
    sorted_genres = sorted(genre_play_count.keys(), key=lambda g: genre_play_count[g], reverse=True)

    # 3. 각 장르에서 상위 두 곡씩 선택
    result = []
    for genre in sorted_genres:
        # 곡 정렬: 재생 횟수 내림차순, 고유 번호 오름차순
        sorted_songs = sorted(songs_by_genre[genre], key=lambda x: (-x[0], x[1]))
        # 상위 두 곡만 선택
        result.extend([song[1] for song in sorted_songs[:2]])

    return result