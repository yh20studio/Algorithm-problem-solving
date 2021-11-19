# link : https://programmers.co.kr/learn/courses/30/lessons/42587
# Lv : 2
# Category : 큐

# 인쇄 중요도를 dictionary로 관리함과 동시에 대기열의 순서대로 출력해야하므로 큐를 이용해서 한다.

from collections import deque

def solution(priorities, location):
    answer = []
    dic = {}
    queue = deque()
    
    for i in range(len(priorities)):
        priority = priorities[i]
        queue.append(i)
        if priority in dic.keys():
            dic[priority].append(i)
        else:
            dic[priority] = [i]
    
    while queue:
        index = queue.popleft()
        priority = priorities[index]
        
        is_to_back = False 
        for key in dic.keys():
            if priority < key:
                is_to_back = True
        
        # 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if is_to_back:
            queue.append(index)
        else:
            answer.append(index)
            
            if len(dic[priority]) > 1:
                dic[priority].remove(index)
            else:
                del(dic[priority])
    
    
    return answer.index(location) + 1