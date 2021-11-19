# link : https://www.acmicpc.net/problem/11049
# Lv : gold 3
# Category : 다이나믹프로그래밍


import sys

N = int(sys.stdin.readline())
mat = []
dp = [[0 for i in range(N)] for i in range(N)]


for i in range(N):
  r, c = map(int, (sys.stdin.readline().split()))
  mat.append([r, c])
  
matrix_cnt = N
max_product = 2 ** 31

for i in range(1, N):
  for j in range(N-i):
    dp[j][j+i] = max_product
    for k in range(j, j+i):
      dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + mat[j][0]*mat[k][1]*mat[j+i][1])
      
print(dp[0][N-1])