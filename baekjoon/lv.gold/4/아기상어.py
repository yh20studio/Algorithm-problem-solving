# link : https://www.acmicpc.net/problem/16236
# Lv : gold 4
# Category : BFS, 우선순위 큐

# 1. 아기상어가 현재 있는 위치에서 먹을 수 있는 먹이까지의 거리들을 bfs를 통해서 구해봅니다.
# 2. 구하고 난후 해당 좌표까지 걸린 (거리, row, column) 순으로 우선순위 큐에 넣어줍니다.
# 3. 그리고 의미없는 반복을 피하기 위하여 maxDistance 값을 설정하여 이보다 많은 거리가 나오면 bfs를 종료하는 것으로 합니다.
# 4. 우선순위 큐에서 가장 앞의 값을 꺼내고 거리값을 더해주고 새로운 row와 column으로 알고리즘을 다시 실행합니다.
# 5. 혹시 아기상어의 레벨업 조건이 충족된다면 레벨업을 시켜줍니다.

import sys
from collections import deque
from heapq import heappop, heappush

def feed(start, scaleCount, babyScale):
  global answer 
  r, c = start
  smallFishies = []
  deq = deque()
  deq.append([r, c, 0])
  visited = []
  maxDist = 400
  while deq:
    r, c, count = deq.popleft()
    if count > maxDist:
      continue
    if board[r][c] <  babyScale and board[r][c] != 0:
      heappush(smallFishies, (count, r, c))
      maxDist = count
    if [r, c] not in visited:
      for i in range(4):
        new_r = r + dy[i]
        new_c = c + dx[i]
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
          continue
        if board[new_r][new_c] <= babyScale:
          deq.append([new_r, new_c, count+1])
      visited.append([r, c])
  
  if len(smallFishies) == 0:
    print(answer)
  else:
    dist, newRow, newColumn = heappop(smallFishies)
    board[newRow][newColumn] = 0
    answer += dist
    scaleCount+=1
    if scaleCount == babyScale:
      scaleCount = 0
      babyScale += 1
    feed([newRow, newColumn], scaleCount, babyScale)

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]
start = [0, 0]

for i in range(N):
  li = list(map(int, sys.stdin.readline().split()))
  for j in range(N):
    if li[j] == 9:
      start = [i, j]
      li[j] = 0  
    board[i][j] = li[j]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
feed(start, 0, 2)