# link : https://programmers.co.kr/learn/courses/30/lessons/17678
# Lv : 3, 2018 KAKAO BLIND RECRUITMENT
# Category : 구현, 우선순위 큐

# 시간에 따라서 대기자가 생기는데, 먼저 대기한 사람이 버스에 먼저 타는 구조이므로, 
# 시간값에 따라서 정리가 되야하므로 우선순위 큐를 활용했다.
# 또한 여러가지 경우의 수를 대비하여 막차시간 때 반복문을 따로 할 수 있도록 했다.

from heapq import heappush, heappop

def solution(n, t, m, timetable):
    answer = ''  
    safe_crew = 0
    last_bus_start_minute = 9*60 + (n-1)*t
    queue = []
    for time in timetable:
        str_h, str_m = time.split(":")
        minute = int(str_h)* 60 + int(str_m)
        if minute <= last_bus_start_minute:
            safe_crew += 1
        heappush(queue, minute)
    
    max_safe_crew = t*m
   
    now = 9*60
    in_bus_crew = 0 
    while now < last_bus_start_minute: # 막차 시간 전까지 태우기
        if in_bus_crew < m:
            minute = heappop(queue)
            if minute <= now: # 기다리는 크루 한명 태움
                in_bus_crew+=1
                safe_crew -= 1
            else: # 더 기다리는 사람이 없으니 버스 출발
                heappush(queue, minute) 
                now += t 
                in_bus_crew = 0
        else: # 버스 정원이 다 찼으니 버스 출발
            now += t 
            in_bus_crew = 0
    
    # 막차 시간일 때 콘이 꼭 타야함
    crew = 0
    while crew < m and queue:
        minute = heappop(queue)
        if minute <= now: # 기다리는 크루 한명 태움
            if m - crew == 1: # 최종적으로 1자리 남았을 때
                answer = minute - 1 # 마지막 사람보다 1분 더 빨리 와야한다.
            crew+= 1
        
    if answer == '':
        answer = now
    
    hour, minute = divmod(answer, 60)            
    
    return f"{hour:02d}:{minute:02d}" # leading Zero