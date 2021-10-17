# link : https://www.acmicpc.net/problem/17143
# Lv : gold
# Category : 구현

import sys  

R, C, M = map(int, (sys.stdin.readline().split()))
board = [[[] for _ in range(C+1)] for _ in range(R+1)]
answer = 0 
fisherman = 1
shark_speed = []
shark_direction = []
shark_size = []
shark_rocation = [[] for _ in range(M)]
# d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

for i in range(M):
  r, c, s, d, z = map(int, (sys.stdin.readline().split()))
  board[r][c].append(i)
  shark_rocation[i] = [r, c]
  shark_speed.append(s)
  shark_direction.append(d)
  shark_size.append(z)

while fisherman <= C:
  # 제일 가까운 상어만 잡고 break!
  for fish_row in range(1, R+1):
    if len(board[fish_row][fisherman]) != 0:
      fished_shark_index = board[fish_row][fisherman].pop()
      shark_rocation[fished_shark_index] = []
      answer+= shark_size[fished_shark_index]
      break
    
  for shark_index in range(M):
    if len(shark_rocation[shark_index]) == 0:
      continue
    
    row, column = shark_rocation[shark_index]
    board[row][column].remove(shark_index)
    d = shark_direction[shark_index]
    s = shark_speed[shark_index]
    new_r = row
    new_c = column
    while s > 0:
      new_r += dy[d]
      new_c += dx[d]
      
      # 위로 방향전환
      if new_r == R+1:
        new_r = R-1
        d = 1
        shark_direction[shark_index] = 1
      
      # 아래로 방향전환
      elif new_r == 0:
        new_r = 2
        d = 2
        shark_direction[shark_index] = 2

      # 오른쪽으로 방향전환
      elif new_c == 0:
        new_c = 2
        d = 3
        shark_direction[shark_index] = 3
      
      # 왼쪽으로 방향전환
      elif new_c == C+1:
        new_c = C-1
        d = 4
        shark_direction[shark_index] = 4

      s -= 1

    board[new_r][new_c].append(shark_index)
    shark_rocation[shark_index] = [new_r, new_c]

  # 모든 상어 이동 후 잡아먹힘 관계
  for i in range(1, R+1):
    for j in range(1, C+1):
      if len(board[i][j]) <= 1:
        continue

      # 가장 큰 상어 찾기
      large_size = 0
      large_shark = -1
    
      for shark in board[i][j]:
        if large_size < shark_size[shark]:
          large_size = shark_size[shark]
          large_shark = shark

      # 나머지 작은 상어 제거
      for s in board[i][j]:
        if s != large_shark:
          shark_rocation[s] = []

      board[i][j] = [large_shark]
      
  
  fisherman+= 1

print(answer)
      