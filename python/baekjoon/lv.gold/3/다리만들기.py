# link : https://www.acmicpc.net/problem/2146
# Lv : gold 3
# Category : BFS

# board, vistited 배열을 두가지 이용해서 board 배열에서는 distance를 표현하기 위해서 각 구역을 구분하지 않고 1칸씩 영역을 넓혀갑니다.
# 영역을 넓히던 도중 다른 구역의 영역을 만날경우 두 지역을 연결하는 다리의 크기를 구할 수 있게됩니다.
# 이때 서로 다른 구역이라는 것을 인지해야하기 때문에 vistited 배열을 이용해서는 영역을 넓힐때마다 자신의 영역이라는 것을 넘버링을 통해서 표시했습니다.

import sys
from collections import deque

def splitGround():
  numbering = 2
  for i in range(N):
    for j in range(N):
      if visited[i][j] != 1:
        continue 
      deq = deque()
      deq.append([i, j])
      visited[i][j] = numbering
      while deq:
        r, c = deq.popleft()
        for v in range(4):
          newRow = r + dy[v]
          newColumn = c + dx[v]

          if newRow < 0 or newRow >= N or newColumn < 0 or newColumn >= N:
            continue

          if visited[newRow][newColumn] == 1:
            visited[newRow][newColumn] = numbering
            deq.append([newRow, newColumn])
      
      numbering += 1

def calculateMinDistance(depth):
  dist = 100001
  for r in range(N):
    for c in range(N):
      if board[r][c] != depth:
        continue 
      numbering = visited[r][c]
      for v in range(4):
        newRow = r + dy[v]
        newColumn = c + dx[v]

        if newRow < 0 or newRow >= N or newColumn < 0 or newColumn >= N:
          continue

        if board[newRow][newColumn] == 0:
          board[newRow][newColumn] = depth + 1
          visited[newRow][newColumn] = numbering
        if board[newRow][newColumn] == depth and visited[newRow][newColumn] != numbering:
          dist = min(dist, (depth-1) * 2)
          
        if board[newRow][newColumn] == depth-1 and visited[newRow][newColumn] != numbering:
          dist = min(dist, board[newRow][newColumn] + depth -2)
  if dist != 1001:
    return dist
  return calculateMinDistance(depth + 1)
N = int(sys.stdin.readline())
board = []
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N): 
  board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
  for j in range(N):
    if board[i][j] == 1:
      visited[i][j] = 1 

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

splitGround()
print(calculateMinDistance(1))