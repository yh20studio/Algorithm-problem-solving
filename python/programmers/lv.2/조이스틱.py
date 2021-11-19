# link : https://programmers.co.kr/learn/courses/30/lessons/42860
# Lv : 2
# Category : 그리디, 구현

# 현재 위치에서 오른쪽과 왼쪽 중 어느 곳으로 갈지 선택해야한다. 이때 최솟값을 구하기 위해서는 방향전환을 많이 하면 안된다.
# 따라서 그리디한 방법으로 최솟값 방향으로 따라가다보면 정답을 구할 수 있다.

from collections import deque

def solution(name):
    answer = 0
    alphabet_index = [
        "A", "B", "C", "D", "E", 
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",       
        "U", "V", "W", "X", "Y", "Z"
    ]
    numberList = []
    need_change = []
    change_cnt = 0
    for v in range(len(name)):
        char = name[v]
        i = alphabet_index.index(char)
        if i != 0 :
            need_change.append(True)
            change_cnt+= 1
        else:
            need_change.append(False)
        
        if i > 13: # N
            numberList.append(26-i)
        else:
            numberList.append(i)
    
    now = 0
    
    if need_change[now] == True:
        answer += numberList[now]
        need_change[now] = False
        change_cnt -= 1
    
    while change_cnt > 0:
        # 다음 위치까지 오른쪽으로 간다고 가정할 때 현재위치에서 몇칸을 가는지 구하기
        first_right = 0
        right = 0
        for i in range(len(need_change)):
            if now+i > len(need_change) -1:
                if need_change[now+i-len(need_change)] == True:
                    first_right = now+i-len(need_change)
                    right = (len(need_change) - now) + first_right
                    break
            else:
                if need_change[now+i] == True:
                    first_right = now+i
                    right = first_right- now
                    break
        
        # 다음 위치까지 왼쪽 간다고 가정할 때 현재위치에서 몇칸을 가는지 구하기
        first_left = 0
        left = 0
        for i in range(len(need_change)):
            if now-i < 0:
                if need_change[now-i+len(need_change)] == True:
                    first_left = now-i+len(need_change)
                    left = (len(need_change) - first_left) + now
                    break
            else:
                if need_change[now-i] == True:
                    first_left = now-i
                    left = now - first_left
                    break
        
        # 현재 위치에서 가장 가까운 곳을 향해서 그리디하게 움직인다.
        if right <= left:
            answer += right
            now = first_right
            need_change[now] = False
            answer += numberList[now]
            
        elif right > left:
            answer += left
            now = first_left
            need_change[now] = False
            answer += numberList[now]

        change_cnt -= 1
   
    return answer