# link : https://www.acmicpc.net/problem/2667
# Lv : silver 1
# Category : BFS

# 아파트끼리 상하좌우로 움직여서 갈 수 있다면 이웃이며 하나의 단지로 명칭할 수 있다고 한다. 
# 따라서 dx, dy를 지정하고 반복문을 통해서 상하좌우로 움직이는 형태를 구현했다. 
# 그리고 조건에 맞게 bfs를 수행하고 각 bfs경로마다 count 값을 계산하여 result라는 배열에 담아준다.

import sys
from collections import deque

def neighborhood():
  result = []
  for r in range(N):
    for c in range(N):
      state = houseMap[r][c]
      if state == 1:
        count = 0
        deq = deque()
        deq.append([r, c])
        while deq:
          row, column = deq.popleft()
          if houseMap[row][column] == 1:
            count += 1
            for i in range(4):
              newRow = row + dy[i]
              newColumn = column + dx[i]

              if newRow < 0 or newRow >= N or newColumn < 0 or newColumn >= N:
                continue
              if houseMap[newRow][newColumn] == 1:
                deq.append([newRow, newColumn])
            houseMap[row][column] = 0
        result.append(count)
  
  return sorted(result)


N = int(sys.stdin.readline())
houseMap = []

for i in range(N):
  houseMap.append(list(map(int, sys.stdin.readline().rstrip('\n'))))


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = neighborhood()

print(len(answer))
for number in answer:
  print(number)