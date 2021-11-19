# link : https://programmers.co.kr/learn/courses/30/lessons/42626
# Lv : 2
# Category : 우선순위 큐

# 요구 조건을 맞추면서 우선순위 큐를 사용하는 것이다.
# 이때 주의해야 하는점이 2개씩 pop을 하다보니, 홍수개가 남았을 때를 잘 처리해야한다.

from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    queue = [] 
    
    for number in scoville:
        heappush(queue, number)
    
    success = False
    while len(queue) >= 2: # 반복문을 진행하기 위해서는 2개 이상 존재해야한다.
        food1 = heappop(queue)
        food2 = heappop(queue)
        
        if food1 >= K and food2 >= K:
            success = True
            break
        else:
            new_food = food1 + food2*2
            heappush(queue, new_food)
            answer += 1
            
    if len(queue) == 1: # 1개의 음식이 남았지만 요구조건을 성공한 경우
        food = heappop(queue)
        if food >= K:
            success = True
    
    if success:
        return answer
    else:
        return -1 # 성공하지 못한다면 -1을 리턴