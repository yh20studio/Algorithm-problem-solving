# https://programmers.co.kr/learn/courses/30/lessons/87694
# Weekly Challenge
# Category : 좌표평면, 구현, BFS

# 캐릭터가 갈 수 있는 borad판을 만들어야 하는데, 주어진 범위인 1~50으로 만들게 되면 캐릭터가 가야하지 않을 방향으로 가는 경우가 생긴다. 
# 예를 들어서 캐릭터는 'ㄷ' 과 'ㅁ' 구조를 구분할 수 없을 것이다.
# 따라서 borad판의 크기를 2배로 제작하여 잘못된 길로 가지 않도록 한다.

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 0 : 빈곳, 1: 직사각형 내부, 2: 직사각형 경계선
    board = [[0 for _ in range(101)] for _ in range(101)]
    
    for left_x, left_y, right_x, right_y in rectangle:
        for x in range(left_x*2, right_x*2+1):
            for y in range(left_y*2, right_y*2+1):
                # 직사각형 경계선
                if x == left_x*2 or x == right_x*2 or y == left_y*2 or y == right_y*2:
                    if board[100 - x + 1][100 - y + 1] == 0:
                        board[100 - x + 1][100 - y + 1] = 2    
                        
                # 직사각형 내부
                else:
                    if board[100 - x + 1][100 - y + 1] == 0:
                        board[100 - x + 1][100 - y + 1] = 1
                    elif board[100 - x + 1][100 - y + 1] == 2:
                        board[100 - x + 1][100 - y + 1] = 1
    
    # 위쪽: 0, 오른쪽: 1, 아래쪽: 2, 왼쪽: 3
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    queue = deque()
    queue.append([characterX*2, characterY*2, 0])
    visited = []
    
    while queue:
        x, y, count = queue.popleft()
        # 목표지점에 도달하면 while 문을 탈출
        if [x, y] == [itemX*2, itemY*2]:
            answer = count//2
            break
            
        if [x, y] not in visited:
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                # 좌표평면을 벗어나지 않는다.
                if new_x <= 100 and new_x >=1 and new_y <= 100 and new_y >=1:
                    # 직사각형의 경계선만 움직인다.
                    if board[100 - new_x + 1][100 - new_y + 1] == 2:
                        queue.append([new_x, new_y, count+1])  
            visited.append([x, y])
    return answer