# link : https://www.acmicpc.net/problem/2206
# Lv : gold 4
# Category : BFS

# bfs 도중에 벽을 부수는 행위를 해야하는 것을 깨닫고
# 벽을 1번만 부수는 조건이므로 벽을 이미 부순 상태로 bfs를 돌고 있는 것과 벽을 부술 기회가 남아 있는 것으로 나누어서 생각했습니다.
# 따라서 visited에 코스트를 저장하고 비교할 때 벽을 이미 부순 그룹 vs 벽 부술 기회가 있는 그룹으로 나누어서 저장했습니다.

from collections import deque

N, M = map(int, input().split())

walls = []
board = []
for i in range(N):  
  board.append([int(_) for _ in input()])

for i in range(N):
  for v in range(M):
    if board[i][v] == 1:
      walls.append([i,v])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
INF = float('inf')

def bfs(board):
  deq = deque()
  deq.append([0,0,1,True])  
  visited =[[INF for _ in range(M)] for _ in range(N)]
  crush_visited =[[INF for _ in range(M)] for _ in range(N)]
  result = []
  while deq:
    r, c, cost, wall = deq.popleft()
    if [r, c] == [N-1, M-1]:
      result.append(cost)
    else:
      for i in range(4):
        new_r = r + dy[i]
        new_c = c + dx[i] 

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
          continue
        
        if wall:
          prev_cost = visited[new_r][new_c]
        else:
          prev_cost = crush_visited[new_r][new_c]

        if board[new_r][new_c] == 0:
          if prev_cost > cost+1:
            deq.append([new_r, new_c, cost+1, wall])
            if wall:
              visited[new_r][new_c] = cost+1
            else:
              crush_visited[new_r][new_c] = cost+1
        else:
          if wall == True: 
            if prev_cost > cost+1:
              deq.append([new_r, new_c, cost+1, False])
              crush_visited[new_r][new_c] = cost+1
        
  if len(result) == 0:
    return -1
  else:
    return min(result)


print(bfs(board))