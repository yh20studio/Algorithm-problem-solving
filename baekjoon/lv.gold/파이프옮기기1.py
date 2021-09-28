# link : https://www.acmicpc.net/problem/17070
# Lv : gold
# Category : dfs, 다이나믹프로그래밍

import sys  

# 가로 움직임
def move_horizontal(r, c):
  if c+1 >= N :
    return False
  elif board[r][c+1] == 1:
    return False
  else:
    return True

# 세로 움직임
def move_vertical(r, c):
  if r+1 >= N:
    return False
  elif board[r+1][c] ==1 :
    return False
  else:
    return True

# 대각선 움직임
def move_diagonal(r, c):
  if c+1 >= N:
    return False
  elif r+1 >= N:
    return False
  elif board[r][c+1] == 1 or board[r+1][c] == 1 or board[r+1][c+1] == 1:
    return False
  else:
    return True

def dfs(r, c, d):
  cnt = 0
  li = []

  if [r, c] == [N-1, N-1]:
    return 1
  if (dp[r][c])[d] == -1:
    return 0
  if (dp[r][c])[d] > 0:
    return dp[r][c][d]

  if direction[d] == "가로":
    if move_horizontal(r, c):
      li.append([r, c+1, 0])
    if move_diagonal(r, c):
      li.append([r+1, c+1, 2])
  elif direction[d] == "세로":
    if move_vertical(r, c):
      li.append([r+1, c, 1])
    if move_diagonal(r, c):
      li.append([r+1, c+1, 2])
  else:
    if move_horizontal(r, c):
      li.append([r, c+1, 0])
    if move_vertical(r, c):
      li.append([r+1, c, 1])
    if move_diagonal(r, c):
      li.append([r+1, c+1, 2])
  
  for new_r, new_c, new_d in li:
    cnt += dfs(new_r, new_c, new_d)

  if cnt == 0:
    (dp[r][c])[d] = -1
  else:
    (dp[r][c])[d] = cnt
  
  return cnt



N = int(sys.stdin.readline())

board = []
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
  li = list(map(int, sys.stdin.readline().split()))
  board.append(li)

direction = ["가로", "세로", "대각선"]
answer = 0
dfs(0, 1, 0)

for number in dp[0][1]:
  if number >0:
    answer+= number

print(answer)