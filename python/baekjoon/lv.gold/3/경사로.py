# link : https://www.acmicpc.net/problem/14890
# Lv : gold 3
# Category : 구현

# 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
# 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
# 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.
# 경사로를 놓은 곳에 또 경사로를 놓는 경우
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
# 경사로를 놓다가 범위를 벗어나는 경우

import sys

N, L = map(int, (sys.stdin.readline().split()))

board = []

for i in range(N):
  board.append(list(map(int, sys.stdin.readline().split())))

result = 0

def slide(i, v, target_number, slide_number, direction):
  count = 0
  li = []
  if direction == 'row':
    for j in range(v, N):
      if target_number == board[i][j] and j not in slide_number:
        count+= 1
        li.append(j)
        if L <= count:
          return li 
      else:
        return False
  else:
    for j in range(v, N):
      if target_number == board[j][i] and j not in slide_number:
        count+= 1
        li.append(j)
        if L <= count:
          return li 
      else:
        return False
  return False

def slide_forward(i, v, target_number, slide_number, direction):
  count = 0
  li = []
  if direction == 'row':
    for j in range(1, v+1):
      if target_number == board[i][v-j] and v-j not in slide_number:
        count+= 1
        li.append(v-j)
        if L <= count:
          return li 
      else:
        return False
  else:
    for j in range(1, v+1):
      if target_number == board[v-j][i] and v-j not in slide_number:
        count+= 1
        li.append(v-j)
        if L <= count:
          return li 
      else:
        return False
  return False

def row_check(r):
  prev_number = 0
  slide_number = []
  for v in range(N):
    if v == 0 :
      prev_number = board[r][v]
    else:
      if prev_number == board[r][v]:
        pass
      else:
        if prev_number - board[r][v] == 1:
            if slide(r, v, board[r][v], slide_number, 'row') == False:
              return False        
            else:
              slide_number.extend(slide(r, v, board[r][v], slide_number, 'row'))
              prev_number = board[r][v]
        elif board[r][v] - prev_number == 1:
            if slide_forward(r, v, prev_number, slide_number, 'row') == False:
              return False        
            else:
              slide_number.extend(slide_forward(r, v, prev_number, slide_number, 'row'))
              prev_number = board[r][v]
        else:
          return False
  return True

def col_check(c):
  prev_number = 0
  slide_number = []
  for v in range(N):
    if v == 0 :
      prev_number = board[v][c]
    else:
      if prev_number == board[v][c]:
        pass
      else:
        if prev_number - board[v][c] == 1:
            if slide(c, v, board[v][c], slide_number, 'col') == False:
              return False        
            else:
              slide_number.extend(slide(c, v, board[v][c], slide_number, 'col'))
              prev_number = board[v][c]
        elif board[v][c] - prev_number == 1:
          if slide_forward(c, v, prev_number, slide_number, 'col') == False:
            return False        
          else:
            slide_number.extend(slide_forward(c, v, prev_number, slide_number, 'col'))
            prev_number = board[v][c]
        else:
          return False
  return True


for i in range(N):
  if row_check(i):
    result+=1
  if col_check(i):
    result+=1

print(result)