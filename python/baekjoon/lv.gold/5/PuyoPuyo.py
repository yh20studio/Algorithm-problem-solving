# link : https://www.acmicpc.net/problem/11559
# Lv : gold 5
# Category : BFS, 구현

# 4개이상의 같은 알파벳이 연결되면 해당 뿌요들이 한번에 터지는 구조이다. 
# 따라서 BFS를 통해서 터질 수 있는 뿌요들을 찾아놓고 한번에 터트려야한다.
# 터트린 이후에는 중력에 의해 아래로 떨어지는 것을 구현한다.

import sys 
from collections import deque

# 총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.
board = []
answer = 0
for _ in range(12):
  rows = list(sys.stdin.readline())[:-1]
  board.append(rows)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
  remove_list = []
  # 터질 [r, c] 찾기
  for i in range(12):
    for j in range(6):
      if board[i][j] != '.' and [i,j] not in remove_list:
        queue = deque()
        queue.append([i, j])
        visited =[]
        now_alphabet = board[i][j]
        while queue:
          r, c = queue.popleft()
          if [r, c] not in visited:
            for direction in range(4):
              new_r = r + dy[direction]
              new_c = c + dx[direction]

              if new_r >= 0 and new_r < 12 and new_c >= 0 and new_c < 6:
                if board[new_r][new_c] == now_alphabet:
                  queue.append([new_r, new_c])

            visited.append([r, c])
      
        if len(visited) >= 4:
          for li in visited:
            remove_list.append(li)
  
  if len(remove_list) == 0: # 더이상 터트릴 뿌요가 없다면 반복 종료
    break
  else:
    for r, c in remove_list: # 뿌요 삭제
      board[r][c] = '.'

    # 삭제 후 중력의 영향
    for c in range(6):
      alphabets = []
      for r in range(12): 
        if board[11-r][c] != '.':
          alphabets.append(board[11-r][c])
          board[11-r][c] = '.'
      
      for i in range(len(alphabets)):
        board[11-i][c] = alphabets[i]

    answer += 1
    
print(answer)

