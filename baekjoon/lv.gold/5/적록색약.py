# link : https://www.acmicpc.net/problem/10026
# Lv : gold 5
# Category : BFS, 구현

# 적록색약인 사람은 R, G를 구분 못하고 같은 것이라 생각하며 일반 사람들은 R, G, B 색을 모두 구분할 수 있다고 합니다.
# 따라서 구역을 나누는 알고리즘이 2번이 사용된다는 것을 느끼고 같은 코드로 적록색약인 사람과 일반 사람들을 각각 1번씩 구하기로 생각했습니다.
# 각 배열의 좌표에서 시작해서 같은 색이라고 생각하는 부분이 나온다면 계속 탐색을 이어나가고 다른 색이 나온다면 탐색을 중지하는 것입니다.
# 이때, check 배열을 활용하여 방문한 곳은 다시 방문하지 않도록 하며, 구역을 구분할 수 있도록 numbering 이라는 변수를 통해서 저장합니다.

import sys
from collections import deque

def rgbTest(person):
  numbering = 1
  check = [[0 for _ in range(N)] for _ in range(N)]

  for i in range(N):  
    for v in range(N):  
      if check[i][v] != 0:
        continue
      color = colors[i][v]
      deq = deque()
      deq.append([i, v])

      while deq:
        r, c = deq.popleft()
        for j in range(4):
          newR = r + dy[j]
          newC = c + dx[j]
          if newR < 0 or newR >= N or newC < 0 or newC >= N:
            continue
          if person == 'Normal':
            if colors[newR][newC] != color:
              continue
          elif person == 'Blindness':
            if color == 'R' or color == 'G':
              if colors[newR][newC] == 'B':
                continue
            elif color == 'B':
              if colors[newR][newC] != 'B':
                continue
          if check[newR][newC] != 0:
            continue
          check[newR][newC] = numbering
          deq.append([newR, newC])
      
      numbering += 1
  
  return numbering - 1

N = int(sys.stdin.readline())
colors = []
for i in range(N):
  colors.append(list(map(str, sys.stdin.readline().strip())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print(f"{rgbTest('Normal')} {rgbTest('Blindness')}")