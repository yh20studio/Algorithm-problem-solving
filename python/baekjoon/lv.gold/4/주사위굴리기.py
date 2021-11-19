# link : https://www.acmicpc.net/problem/14499
# Lv : gold 4
# Category : 구현

import sys

N, M, y, x, K  = map(int, sys.stdin.readline().split())

board = []

for i in range(N):
  board.append(list(map(int, sys.stdin.readline().split())))

order_list = list(map(int, sys.stdin.readline().split()))

dice = [0, 0, 0, 0, 0, 0]

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for order in order_list:
  new_y = y + dy[order-1]
  new_x = x + dx[order-1]
  if new_y <0 or new_y>= N or new_x <0 or new_x >= M:
    continue

  y = new_y
  x = new_x

  if order == 1:
    dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
  elif order == 2:
    dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
  elif order == 3:
    dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
  else:
    dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
  
  if board[y][x] == 0:
    board[y][x] = dice[5]
  else:
    dice[5] = board[y][x]
    board[y][x] = 0

  print(dice[0])