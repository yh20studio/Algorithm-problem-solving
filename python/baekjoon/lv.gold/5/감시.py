# link : https://www.acmicpc.net/problem/15683
# Lv : gold 5
# Category : DFS

# 각 CCTV의 모양에 따라서 감시할 수 있는 방향이 달라진다. 이때 CCTV가 감시할 수 있는 영역을 최대로 늘리는 문제이다.
# 각각의 CCTV는 서로의 방향에 따라서 영역을 최대로 늘리는 감시방향을 선택할 때 영향을 받으므로 
# 모든 경우를 탐색하는 것이 더 좋다고 생각했다.
# 그리하여 DFS 방법을 선택했고, 한 방향의 탐색이 끝나면 Office의 상태를 원래대로 돌려놓도록 구현하여 
# 이전 탐색이 다음 탐색의 영향을 끼치지 않도록 했다.

import sys  

def countSapce(N, M):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if office[i][j] == 0:
        cnt+= 1
  return cnt

def checkCCTV(direction, r, c, N, M):
  li = []
  for i in direction:
    new_r = r+ dy[i]
    new_c = c+ dx[i]
    while 0 <= new_r and new_r < N and 0 <= new_c and new_c < M:
      if office[new_r][new_c] == 0: 
        office[new_r][new_c] = '#'
        li.append([new_r, new_c])
      elif office[new_r][new_c] == 6: 
        break
      new_r += dy[i]
      new_c += dx[i]
  
  return li


def dfs(index, N, M):
  global answer

  if index == len(cctvs): # 모든 CCTV의 방향을 결정했다면 비감시 영역의 최솟값을 도출한다.
    answer = min(answer, countSapce(N, M))
  
  else:
    r, c = cctvs[index]
    cctv = office[r][c]

    if cctv == 1:
      cctv_type = [[0], [1], [2], [3]]
   
    elif cctv == 2:
      cctv_type = [[0, 2], [1, 3]]
      
    elif cctv == 3:
      cctv_type = [[0, 1], [1, 2], [2, 3], [3, 0]]

    elif cctv == 4:
      cctv_type = [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]]

    else:
      cctv_type = [[0, 1, 2, 3]]

    for direction in cctv_type: 
      back = checkCCTV(direction, r, c, N, M)
      dfs(index+1, N, M)
      for back_r, back_c in back: # 탐색이 끝나면 원래대로 돌려놓기
        office[back_r][back_c] = 0

global answer
answer = 65 # Office의 최대 영역이 64

N, M = map(int, sys.stdin.readline().split()) # (1 ≤ N, M ≤ 8)

office = []
cctvs = []

for _ in range(N):
  office.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
  for j in range(M):
    if office[i][j] != 0 and office[i][j] != 6:
      cctvs.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

dfs(0, N, M)

print(answer)

