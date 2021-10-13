# link : https://programmers.co.kr/learn/courses/30/lessons/62050
# Lv : 4
# Category : 우선순위 큐, 탐색

# [0, 0]에서 시작하여 이동할 수 있는 경우에만 탐색을 계속 진행하는 방식으로 한다.
# 이때 진행이 불가능 하다면, 사다리의 값을 우선순위 큐에 넣어주며, 더이상 진행할 수 있는 땅이 없다면 우선순위 큐에서 가장 작은 사다리
# 비용을 가지도록 사다리를 만들어준 후 다시 그 좌표에서 탐색을 진행하도록 한다.

from collections import deque
from heapq import heappop, heappush

def solution(land, height):
    answer = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n = len(land)
    board = [[0 for _ in range(n)] for _ in range(n)]
    section = 1
    queue = deque()
    queue.append([0, 0])
    ladder = []
    
    while queue:
        r, c = queue.popleft()
        if board[r][c] == 0:
            for i in range(4):
                new_r = r + dy[i]
                new_c = c + dx[i]

                if 0 <= new_r and new_r < n and 0 <= new_c and new_c < n:
                    if abs(land[r][c] - land[new_r][new_c]) <= height:
                        queue.append([new_r, new_c])
                    else:
                        # 다음 땅으로 이동할 수 없는 경우 사다리 비용에 따라서 우선순위 큐에 저장
                        heappush(ladder, [abs(land[r][c] - land[new_r][new_c]), new_r, new_c])
        
            board[r][c] = section
        
        # 더이상 진행할 수 있는 땅이 없는 경우 최소 비용으로 사다리를 건설한다
        if len(queue) == 0:
            while ladder:
                h, r, c = heappop(ladder)
                if board[r][c] == 0:
                    answer += h
                    queue.append([r, c])
                    break            
       
    return answer