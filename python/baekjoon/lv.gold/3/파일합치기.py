# link : https://www.acmicpc.net/problem/11066
# Lv : gold 3
# Category : 다이나믹프로그래밍

# 의미 없는 반복계산을 줄이기 위해서 dp 배열을 만들고 (시작지점, 끝나는 지점)을 이용해서 계산을 할때마다 배열에 저장하는 방식을 선택했다.
# 만약 재귀함수를 도는 도중에 이미 dp 배열에 저장했던 계산이 나온다면 더이상의 계산을 하지 않고 dp 배열 값을 return 하도록 했다.

import sys

def dynamic(start, end):
  if dp[start][end] != 0:
    return dp[start][end]
  
  if start == end:
    cost = files[start]
    dp[start][end] = cost
    return cost

  prev_sum = 0
  cost = float('inf')
  for i in range(start, end+1):
    prev_sum += files[i]

  for v in range(start, end):
    cost = min(cost, prev_sum + dynamic(start, v) + dynamic(v+1, end))

  dp[start][end] = cost
  return cost

T = int(sys.stdin.readline())
result = []
dp = [[0 for _ in range(T)] for _ in range(T)]

for i in range(T):
  K = int(sys.stdin.readline())
  files = list(map(int,sys.stdin.readline().split()))
  dp = [[0 for _ in range(K)] for _ in range(K+1)]
  cost = float('inf')

  for v in range(K):
    cost = min(cost, dynamic(0, v) + dynamic(v+1, K-1)) 
  result.append(cost)
  
for r in result:
  print(r)