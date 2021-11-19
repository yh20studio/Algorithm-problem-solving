# link : https://www.acmicpc.net/problem/2225
# Lv : gold 5
# Category : 다이나믹프로그래밍

import sys

N, K = map(int, (sys.stdin.readline().split()))

if N <= K:
  length = K
else:
  length = N
dp = [[0 for i in range(length+1)] for i in range(length+1)]

for n in range(1, length+1):
  if n == 1:
    for m in range(1, length+1):
      dp[n][m] = m
  else:
    for m in range(1, length+1):
      if m == 1: 
        dp[n][m] = 1
      else:
        dp[n][m] = dp[n][m-1] + dp[n-1][m]

print(dp[N][K]%1000000000)