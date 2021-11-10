# link : https://programmers.co.kr/learn/courses/30/lessons/1844
# Lv : 2, 찾아라 프로그래밍 마에스터
# Category : BFS

# 이 문제는 목표지점까지 최단경로를 찾는 문제이므로 BFS를 이용해서 탐색하며, 목표지점에 도달하면 반복문을 멈추도록 했습니다.
# 이때 방문관리를 하기 위해서 visited를 이용하여 중복된 곳을 방문하지 않도록 했습니다. 
# 방문관리시 리스트를 이용하면 쉽게 코딩되지만 시간을 많이 잡아먹기에 효율성 테스트에서 통과하지 못할 것입니다.

from collections import deque

def solution(maps):
    answer = 0
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    n = len(maps) - 1
    m = len(maps[0]) - 1
    queue = deque()
    queue.append([0, 0, 1])
    visited =[[False for _ in range(m+1)] for _ in range(n+1)]
    while queue:
        r, c, cnt = queue.popleft()
        if [r, c] == [n, m]:
            answer = cnt
            break
            
        if visited[r][c] == False:
            for i in range(4):
                new_r = r + dy[i]
                new_c = c + dx[i]
                
                if new_r >= 0 and new_r <= n and new_c >= 0 and new_c <= m:
                    if maps[new_r][new_c] == 1:
                        queue.append([new_r, new_c, cnt+1])
            
            visited[r][c] = True
    
    if answer == 0: # 목표지점까지 도달하지 못할 때
        return -1
    else:
        return answer