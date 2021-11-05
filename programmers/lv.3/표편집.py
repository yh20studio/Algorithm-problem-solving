# link : https://programmers.co.kr/learn/courses/30/lessons/81303
# Lv : 3, 2021 카카오 채용연계형 인턴십
# Category : 구현, 해시

# 파이썬의 dictionary를 이용해서 구현했다. 각 index에 도착하면 위로가는 경우와 아래로 가는 경우가 있는데
# dictionary에 각 index마다 위로갔을 때 도착할 index, 아래로 갔을 때 도착할 index를 저장한다.
# 삭제와, 되돌리기가 발생할 때 행동이 일어나는 index를 기준으로 아래, 위 index 값의 dictionary를 수정하면서 나아가면된다.

def solution(n, k, cmd):
    idList = [True for i in range(n)]
    upSide = {i:i-1 for i in range(n)}
    downSide = {i:i+1 for i in range(n)}
    last_delete = []
    select = k
    
    for cm in cmd:
        li = cm.split(" ")
   
        if li[0] == "U":
            cnt = int(li[1])
            while cnt > 0:
                select = upSide[select]
                cnt -= 1
                
        elif li[0] == "D":
            cnt = int(li[1])
            while cnt > 0:
                select = downSide[select]
                cnt -= 1
            
            
        elif li[0] == "C":
            idList[select] = False       
            last_delete.append(select)
            up = upSide[select]
            down = downSide[select]
            
            if up > -1:
                downSide[up] = down
                
            if down < n:
                upSide[down] = up
            
            if down == n:
                select = up
            else:
                select = down
                
        elif li[0] == "Z": 
            delete = last_delete.pop()
            idList[delete] = True       
            down = downSide[delete]
            up = upSide[delete]

            if up > -1:
                downSide[up] = delete
            
            if down < n:
                upSide[down] = delete
    
    answer = []        
    for num in idList:
        if num == True:
            answer.append("O") 
        else:
            answer.append("X")
    
    return "".join(answer)