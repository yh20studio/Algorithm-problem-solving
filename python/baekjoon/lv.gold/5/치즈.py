# link : https://www.acmicpc.net/problem/2636
# Lv : gold 5
# Category : BFS, 구현

# 치즈에는 구멍이 있어서 공간으로 공기가 들어가면 치즈가 녹는다. 하지만 구멍에 공기가 접근할 수 없다면 그 부분은 녹지 않는다.
# 따라서 BFS를 이용해서 현재 공기와 닿는 치즈 부분만 탐색하여 녹이고, 모든 치즈가 녹을때까지 BFS를 진행하면 된다.
# BFS 탐색시에 치즈와 만난다면 queue에 넣지 않는 방법으로 치즈를 뚫어서 탐색할 수 없도록 했다.

import sys  
from collections import deque

# 판의 세로와 가로의 길이가 양의 정수로 주어진다. 세로와 가로의 길이는 최대 100이다. 
board_R, board_C = map(int, sys.stdin.readline().split())
board = []
number_of_cheese = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 치즈가 없는 칸은 0, 치즈가 있는 칸은 1로 주어지며 각 숫자 사이에는 빈칸이 하나씩 있다.
for i in range(board_R): 
  li = list(map(int, sys.stdin.readline().split()))
  for is_cheese in li:
    if is_cheese == 1:
      number_of_cheese += 1
  
  board.append(li)

# [녹이는데 걸리는 시간, 바로 직전에 남아있었던 치즈의 개수]
answer = [0, number_of_cheese]
start = [0, 0] # 시작 위치

while True:
  queue = deque()
  queue.append(start)
  melt_cheese = []

  visited =[[0 for _ in range(board_C)] for _ in range(board_R)]
  while queue:
    r, c = queue.popleft()
    if visited[r][c] == 0: # 방문하지 않은 빈공간이라면?
      for i in range(4):
        new_r = r + dy[i]
        new_c = c + dx[i]

        if new_r >= 0 and new_r < board_R and new_c >= 0 and new_c < board_C:
          if board[new_r][new_c] == 1:
            if [new_r, new_c] not in melt_cheese:
              melt_cheese.append([new_r, new_c])
          elif board[new_r][new_c] == 0:
            queue.append([new_r, new_c])

      visited[r][c] = -1

        
  if len(melt_cheese) != 0:
    for i in range(len(melt_cheese)): # 치즈 녹이기
      cheese_r, cheese_c = melt_cheese[i]
      if i ==0:
        start = [cheese_r, cheese_c]
      board[cheese_r][cheese_c] = 0
  
    answer[0] += 1 # 시간 추가
    answer[1] = number_of_cheese # 치즈를 녹이기 전 남은 치즈 수 저장
    number_of_cheese -= len(melt_cheese)
  
  else:
    print(answer[0])
    print(answer[1])
    break

