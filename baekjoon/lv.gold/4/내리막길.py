# link : https://www.acmicpc.net/problem/1520
# Lv : gold 4
# Category : DFS

# 1. dfs를 통해서 되는 경로를 한개 찾는다.
# 2. 재귀함수를 이용한 dfs이므로 정답이 되는 경로 바로 직전 좌표에서 다시 탐색을 하기 시작한다.
# 3. 해당 경로에서 탐색이 끝났다면 재귀함수를 종료한다.
# 4. 만약 해당 경로로 도착지로 갈 수 있다면 dp 리스트에 가능한 경로의 수를 저장한다.
# 5. 이떄 저장하는 경로의 수는 이미 계산되어 저장되어 있는 내리막길에 따라서 가는 다음 경로의 dp 리스트의 값을 이용한다.
# 6. 만약 재귀함수를 돌다가 dp 리스트에서 0, -1 이 아닌 다른 값을 만나게 된다면 해당 좌표로 부터 도착지점까지 도착할 수 있다는 뜻으로 재귀함수를 종료하게 된다

import sys

def dfs(r, c):
  if [r, c] == [M-1, N-1]:
    dp[r][c] = 1
    return True
  if dp[r][c] > 0:
    return True
  if dp[r][c] < 0:
    return False
  else:
    goal = False
    for i in range(4):
      new_r = r + dy[i]
      new_c = c + dx[i]
      if new_r < 0 or new_r >= M or new_c < 0 or new_c >= N:
        continue
      else:
        if board[r][c] <= board[new_r][new_c]:
          continue
        else:
          if dfs(new_r, new_c):
            dp[r][c] += dp[new_r][new_c]
            goal = True
          else:
            dp[new_r][new_c] = -1
    return goal          
M, N = map(int, sys.stdin.readline().split())
board = []

for _ in range(M):
  board.append(list(map(int, sys.stdin.readline().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dp = [[0 for _ in range(N)] for _ in range(M)]
answer = 0
dfs(0, 0)
print(dp[0][0])