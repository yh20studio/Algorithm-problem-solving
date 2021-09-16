# link : https://programmers.co.kr/learn/courses/30/lessons/85002
# Weekly Challenge
# Category : 구현, 우선순위 큐

from heapq import heappush, heappop

def solution(weights, head2head):
    answer = []
    maxBoxerNumber = 1000
    records = []
    
    for i in range(len(weights)):
        win = 0
        loose = 0 
        bigWin = 0
        for j in range(len(weights)):
            if head2head[i][j] == 'W' :
                if weights[i] < weights[j]:
                    bigWin += 1  
                win += 1
            elif head2head[i][j] == 'L' :
                loose += 1
        
        if (win + loose) == 0:
            record = [0, bigWin, weights[i], maxBoxerNumber - i]    
        else:
            record = [win/(win+loose), bigWin, weights[i], maxBoxerNumber - i]            
        print(record)
        heappush(records, record)
    
    while records:
        boxerIndex = 1000 - heappop(records)[3] + 1
        answer.append(boxerIndex)
    
    answer.reverse()
    
    return answer