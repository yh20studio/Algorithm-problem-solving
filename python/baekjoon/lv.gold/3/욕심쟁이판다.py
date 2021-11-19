# link : https://www.acmicpc.net/problem/1937
# Lv : gold 3
# Category : DFS, 다이나믹프로그래밍

# visited라는 리스트를 두고 하더라도 bfs를 통한 탐색이 최장 생존 경로를 보장해주지는 않습니다.
# 그리하여 재귀함수를 통해서 각 선택에 대한 최장 생존 경로를 찾으려고 했습니다. dp라는 리스트를 만들고 반복되는 계산을 피했습니다.
# 따라서 dp 리스트에는 각 좌표에 도착했을 때 갈 수 있는 최장 생존 경로를 알려줍니다. 
# 그렇게 되면 새로운 좌표에서 판다가 시작을 하더라도 이미 계산한 dp 좌표에 도달하게 되면 해당값을 더하면서 재귀함수가 종료되게 됩니다.
# 그리고 판다는 이전보다 많은 대나무가 있는 곳으로만 가기 때문에 이미 지나온 경로를 다시 가는 사례는 발생하지 않으므로 visited라는 리스트를 따로 관리할 필요가 없는 것입니다.

import sys

N = int(sys.stdin.readline())
board = []

for i in range(N):
  board.append(list(map(int,sys.stdin.readline().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def recursive():  
  result = 0
  for i in range(N):
    for v in range(N):
      dfs(i, v)
      result = max(result, dp[i][v])
  print(result)

def dfs(r, c):  
  find = False
  for i in range(4):
    new_r = r + dy[i]
    new_c = c + dx[i]
    if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
      continue
    else:
      if board[r][c] < board[new_r][new_c]:
        find = True
        if dp[new_r][new_c] != 0:
          dp[r][c] = max(dp[r][c], dp[new_r][new_c]+1)
        else:
          dp[r][c] = max(dp[r][c], dfs(new_r, new_c)+1)
  
  if find == False:
    dp[r][c] = 1
  return dp[r][c]

recursive()