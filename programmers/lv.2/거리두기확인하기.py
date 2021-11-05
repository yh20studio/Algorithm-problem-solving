# link : https://programmers.co.kr/learn/courses/30/lessons/81302
# Lv : 2, 2021 카카오 채용연계형 인턴십
# Category : 구현, BFS

# P는 응시자가 앉아있는 자리를 의미합니다.
# O는 빈 테이블을 의미합니다.
# X는 파티션을 의미합니다.
# BFS로 맨해튼 거리가 2인 구간만 check해주어야한다. 이때 파티션을 만나면 탐색을 더이상 하지 않도록 한다. 
# 탐색중에 한번이라도 다른 응시자를 만나면 이 대기실은 거리두기를 지키지 않고 있는 것으로 간주한다.


from collections import deque

def is_separate(r, c, board, dr, dc):    
    queue = deque()
    queue.append([r, c, 0])
    visited = []
    while queue:
        row, column, count = queue.popleft()

        if count < 2: # 맨해튼 거리가 2 이하
            for i in range(4):
                new_r = row + dr[i]
                new_c = column + dc[i]

                if new_r >= 0 and new_r < 5 and new_c >= 0 and new_c < 5:
                    if [new_r, new_c] not in visited:
                        # 거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
                        if board[new_r][new_c] == "P": 
                            return False
                        elif board[new_r][new_c] == "O":
                            queue.append([new_r, new_c, count+1])

            visited.append([r, c])
    
    return True


def solution(places):
    answer = []
    
    dr = [-1, 0 ,1, 0]
    dc = [0, 1, 0, -1]
    
    for place in places:
        board = []
        for string in place:
            board.append(list(string))
        check = True
            
        for r in range(5):
            for c in range(5):
                if board[r][c] == "P":
                    if is_separate(r, c, board, dr, dc) == False:
                        check = False
                        break
            if check == False:
                break
                
        # 각 대기실별로 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 배열에 담아 return 
        if check: 
            answer.append(1)
        else:
            answer.append(0)
        
    return answer