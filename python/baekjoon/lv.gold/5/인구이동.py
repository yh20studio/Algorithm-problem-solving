# link : https://www.acmicpc.net/problem/16234
# Lv : gold 5
# Category : BFS

import sys  
from collections import deque

def openBorder(L, R):
  need_open = False # 인구 이동이 필요한가?
  # 방문 안했으면 0, 방문했으면 -1로 표시
  visited_total = [[0 for _ in range(N)] for _ in range(N)] 
  for i in range(N):
    for j in range(N):  
      queue = deque()
      queue.append([i, j])
      visited = []
      total_people = 0
      while queue:
        r, c = queue.popleft()
        if visited_total[r][c] != -1:
          total_people += board[r][c]
          for direction in range(4):
            new_r = r+ dy[direction]
            new_c = c+ dx[direction]
            if new_r >= 0 and new_r < N and new_c >= 0 and new_c < N:
              if abs(board[r][c] - board[new_r][new_c])>= L and abs(board[r][c] - board[new_r][new_c]) <= R:
                queue.append([new_r, new_c])
                need_open = True 
          
          visited_total[r][c] = -1
          visited.append([r, c])

      if len(visited) > 1: # 인구 같은 숫자로 이동한다
        divide_people = total_people//len(visited)
        for r, c in visited:
          board[r][c] = divide_people

  return need_open

# N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
N, L, R = map(int, sys.stdin.readline().split())
answer = 0
board = []
for i in range(N):
  board.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while openBorder(L, R) == True: # 인구이동이 일어났다
  answer+=1

print(answer)

