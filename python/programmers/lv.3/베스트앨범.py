# link : https://programmers.co.kr/learn/courses/30/lessons/42579
# Lv : 3
# Category : 우선순위 큐, 해시

# 각 장르마다 재생된 횟수를 모두 구하고, 가장 많이 재생된 장르순으로 나타내야한다.
# 가장 많이 재생된 장르 순으로 부터 해당 장르에서 가장 많이 재생된 곡을 2곡까지 리턴하면 된다.
# 이 2가지 sort하는 과정을 우선순위 큐를 활용해서 했다.

from heapq import heappush, heappop

def solution(genres, plays):
    answer = []
    length = len(genres)
    total_play = {}
    genre_play = {}
    
    for i in range(length):
        genre = genres[i]
        play = plays[i]
        
        if genre in total_play:
            total_play[genre] += play
        else:
            total_play[genre] = play
        
        if genre in genre_play:
            heappush(genre_play[genre], [-play, i])
        else:
            q = []
            heappush(q, [-play, i])
            genre_play[genre] = q
            
    
    queue = []
    
    for key, value in total_play.items():
        heappush(queue, [-value, key])
        
    while queue:
        genre = heappop(queue)[1]
        
        count = 0
        while genre_play[genre] and count < 2:
            index = heappop(genre_play[genre])[1]
            answer.append(index)
            count += 1
    
    return answer