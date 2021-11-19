# link : https://www.acmicpc.net/problem/3190
# Lv : gold 5
# Category : 큐, 구현

# 뱀의 위치를 모두 저장하는 방식이 아니라 큐를 이용해서 뱀의 머리와 꼬리를 추적할 수 있는 방식으로 진행했다.

import sys  
from collections import deque

# 보드의 크기 N (2 ≤ N ≤ 100)
N = int(sys.stdin.readline())
# 사과의 개수 K (0 ≤ K ≤ 100)
K = int(sys.stdin.readline())

board = [[0 for _ in range(N+1)] for _ in range(N+1)]

# board 에 사과는 1로 표시한다.
for _ in range(K):
  r, c = map(int, (sys.stdin.readline().split()))
  board[r][c] = 1

# 뱀의 방향 변환 횟수 L (1 ≤ L ≤ 100)
L = int(sys.stdin.readline())

direction_chages = {}

for _ in range(L):
  x, direction = map(str, (sys.stdin.readline().split()))
  direction_chages[x] = direction

# 뱀은 board에 2로 표시한다.
board[1][1] = 2

snake = deque()
snake.append([1, 1])

# 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
snake_direction = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

second = 1

while snake:
  # X초가 지난 후에 방향을 바꾸는 것이므로 현재 second에서 1을 빼준 것으로 계산한다.
  if f"{second-1}" in direction_chages.keys():
    if direction_chages[f"{second-1}"] == "L": # 왼쪽 90도 회전
      if snake_direction == 0:
        snake_direction = 3
      else:
        snake_direction -=1
    elif direction_chages[f"{second-1}"] == "D": # 오른쪽 90도 회전
      if snake_direction == 3:
        snake_direction = 0
      else:
        snake_direction +=1
      
  head_r, head_c = snake.pop()
  snake.append([head_r, head_c])

  new_head_r = head_r + dy[snake_direction]
  new_head_c = head_c + dx[snake_direction]

  if new_head_r == N+1 or new_head_r == 0 or new_head_c == N+1 or new_head_c == 0:
    break

  else:
    # 사과를 만나면?
    if board[new_head_r][new_head_c] == 1:
      board[new_head_r][new_head_c] = 2      
      snake.append([new_head_r, new_head_c])
      
    # 빈공간을 만나면?
    elif board[new_head_r][new_head_c] == 0:
      board[new_head_r][new_head_c] = 2
      snake.append([new_head_r, new_head_c])

      tail_r, tail_c = snake.popleft()
      board[tail_r][tail_c] = 0

    # 자신의 몸을 만나면?
    elif board[new_head_r][new_head_c] == 2:
      break
  
  second += 1

print(second)
