# link : https://www.acmicpc.net/problem/3190
# Lv : gold 5
# Category : BFS, 구현

# 주어진 땅과 물 에서 가능한 최단 경로 중에서 가장 최댓값을 구하는 문제이다.
# 나누어져 있는 땅에서 가능한 최단 경로를 구해야하는데 이를 BFS를 이용해서 구했다. 이때 이러한 경로중 최댓값을 구하기 위해서는
# 출발지점과 도착지점을 선정하는 것이 중요하다. 그래서 모든 땅인 좌표에서 시작을해서 경로를 구하고, 이 중에서 최댓값을 구하면
# 정답이 될것이다.

import sys  
from collections import deque

def is_blocked(row, column, visited):
  next_land_list = []
  for i in range(4):
    new_r = row+dy[i]
    new_c = column+dx[i]

    if new_r >=0 and new_r < R and new_c >=0 and new_c < C:
      if treasure[new_r][new_c] == "L" and visited[new_r][new_c] == 0:
        next_land_list.append([new_r, new_c])
  
  return next_land_list
    
answer = 0
# 보물 지도의 가로, 세로의 크기는 각각 50이하이다.
R, C = map(int, sys.stdin.readline().split())
treasure = []
for _ in range(R):
  treasure.append(list(sys.stdin.readline())[:-1])


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(R):
  for j in range(C):
    if treasure[i][j] == 'L':
      visited = [[0 for _ in range(C)] for _ in range(R)]        
      queue = deque()
      queue.append([i, j, 0])
      
      while queue:
        row, column, distance = queue.popleft()
        if treasure[row][column] == "L" and visited[row][column] == 0:
          next_land_list = is_blocked(row, column, visited)
          if len(next_land_list) == 0:
            answer = max(answer, distance)
          else:
            for new_r, new_c in next_land_list:
                queue.append([new_r, new_c, distance+1])
                
            visited[row][column] = 1
    
print(answer)