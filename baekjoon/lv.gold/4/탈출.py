# link : https://www.acmicpc.net/problem/3055
# Lv : gold 4
# Category : BFS

# 방문을 통해서 순차적으로 물과 고슴도치가 퍼져나가는 것으로 구현하려고 했으나, 1스텝씩 행동이 일어난 후 다음 행동의 위치를 찾기 위해 반복문을 돌아야 하므로
# 방문 처리를 통해서 관리하는 것보다 큐를 이용하는 것이 시간이 적게 걸린다고 생각했습니다.
# 물, 고슴도치의 위치를 나타낼 수 있는 큐를 2개 생성하여 BFS를 활용한다.
# 이때 고슴도치는 다음 행동에 물이 올 위치에는 가지 못하므로 탐색을 이용할 때 물을 우선으로 움직여야한다.


import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())
board = []

for _ in range(R):
  board.append(list(str(sys.stdin.readline()))[:-1])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def findGoal():
  answer = 0
  water_queue = deque()
  location_queue = deque()

  for i in range(R):
    for j in range(C):
      if board[i][j] == "*":
        water_queue.append([i, j])
      elif board[i][j] == "S":
        location_queue.append([i, j])

  while location_queue:
    for i in range(len(water_queue)):
      i, j = water_queue.popleft()

      for direction in range(4):
        new_r = i + dy[direction]
        new_c = j + dx[direction]

        if new_r >= 0 and new_r < R and new_c >= 0 and new_c < C:
          if board[new_r][new_c] == "." or board[new_r][new_c] == "S":
              board[new_r][new_c] = "*"
              water_queue.append([new_r, new_c])

    for i in range(len(location_queue)):
      i, j = location_queue.popleft()
      
      for direction in range(4):
        new_r = i + dy[direction]
        new_c = j + dx[direction]

        if new_r >= 0 and new_r < R and new_c >= 0 and new_c < C:
          if board[new_r][new_c] == ".":
              board[new_r][new_c] = "S"
              location_queue.append([new_r, new_c])
          
          elif board[new_r][new_c] == "D":
            return answer+1

      board[i][j] == "."

    answer += 1
  return "KAKTUS"

print(findGoal())