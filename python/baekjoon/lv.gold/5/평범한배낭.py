# link : https://www.acmicpc.net/problem/12865
# Lv : gold 5
# Category : 다이나믹프로그래밍, 배낭 알고리즘

# 다이나믹프로그래밍을 활용한 배낭 알고리즘으로 문제를 풀어야 편하다. 처음에는 우선순위 큐, 배열 등으로 해결하려고 하지만 어렵다.

import sys  

# 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
N, K = map(int, (sys.stdin.readline().split()))
answer = 0
weights = [0,]
values = [0,]

# 입력 받기
for _ in range(N):
  W, V = map(int, (sys.stdin.readline().split()))
  weights.append(W)
  values.append(V)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1): # i : 물품의 index
  for j in range(K+1): # j: 배낭에 넣을 수 있는 무게
    if weights[i] > j : # 현재 물품의 무게를 고려할 때 배낭에 넣을 수 없다면
      dp[i][j] = dp[i-1][j] # 이전 row의 dp값을 그대로 따라간다.
    
    elif weights[i] <= j :  # 현재 물품의 무게를 고려할 때 배낭에 넣을 수 있다면
      # max(넣으려는 물품의 가치 + (이전 row의 dp값 중 넣으려고 하는 weight 값을 제거한 Column 값과), 이전 row의 dp 값)
      dp[i][j] = max(values[i] + dp[i-1][j-weights[i]], dp[i-1][j]) 
      answer = max(answer, dp[i][j])

print(answer)