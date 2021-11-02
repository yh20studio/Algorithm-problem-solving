# link : https://www.acmicpc.net/problem/14719
# Lv : gold 5
# Category : 구현


# 물이 고일 수 있는 자리는 양쪽에 벽이 존재해야한다. 따라서 board판에 빈공간과 벽공간을 표현한 후
# 한 row씩 탐섹하면서 양쪽이 벽에 막혀있는 공간의 개수를 카운팅 하면 된다.

import sys  

answer = 0
# 세로 길이 H과 가로 길이 W가 주어진다. (1 ≤ H, W ≤ 500)
H, W = map(int, sys.stdin.readline().split())

# 1: 벽 , 0: 빈공간
board = [[ 0 for _ in range(W)] for _ in range(H)]

heights = list(map(int, sys.stdin.readline().split()))
for w in range(len(heights)):
  h = heights[w]
  for j in range(h):
    board[j][w] = 1

for li in board:
  water = 0
  left_wall = False
  for i in li:
    if left_wall == False:
      if i == 1:
        left_wall = True
    else:
      if i == 0 :
        water += 1
      else: # 오른 벽을 만난다면?
        answer += water
        water = 0

print(answer)

