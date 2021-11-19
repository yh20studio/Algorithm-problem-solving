# link : https://www.acmicpc.net/problem/2580
# Lv : gold 4
# Category : 백트래킹

# 재귀함수로 dfs를 구하여 자식노드들이 차례대로 재귀함수가 끝나면서 스도쿠판을 스스로 복귀시키면서 함수를 종료하도록 한다.

import sys

board = []
zero = []

row_sum = [0 for _ in range(9)]
column_sum = [0 for _ in range(9)]
rec_sum = [0 for _ in range(9)]

for i in range(9):  
  board.append(list(map(int, input().split())))

for i in range(9):
  for v in range(9):
    if board[i][v] == 0 :
      zero.append([i, v])

def check(index, r, c):
  number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
  
  for i in range(9):
    if board[r][i] in number_set:
      number_set.remove(board[r][i])
    if board[i][c] in number_set:
      number_set.remove(board[i][c])

  for i in range(r - r%3 , r - r%3 +3):
    for v in range(c- c%3 , c- c%3 +3):
      if board[i][v] in number_set:
        number_set.remove(board[i][v])
  
  return number_set

def dfs(index, number):
  global reset

  if index != 0:
    prev_r, prev_c = zero[index - 1]
    board[prev_r][prev_c] = number
  
  if index == len(zero):
    for n in range(9):
      print(" ".join(map(str, board[n])))
    sys.exit()
  
  r, c = zero[index]

  for number in check(index, r, c):
    board[r][c] = number
    dfs(index+1, number)
    board[r][c] = 0


dfs(0, 0)