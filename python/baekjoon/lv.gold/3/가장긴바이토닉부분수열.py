# link : https://www.acmicpc.net/problem/11054
# Lv : gold 3
# Category : 다이나믹프로그래밍

# 정방향으로 오름차순을 만족하는 최대 개수를 dp에 저장
# 역방향으로 오름차순을 만족하는 최대 개수를 dp_inverse에 저장
# dp 와 dp_inverse를 인덱스 순으로 더했을 때 최대값을 구함
# 바이토닉 수열에서 최대값인 코어값은 dp와 dp_inverse가 겹치게 카운팅을 했으므로 result에서 -1을 해줌

import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]
dp_inverse = [0 for _ in range(N)]

for i in range(N):
  for v in range(i):
    if numbers[i] > numbers[v]:
      dp[i] = max(dp[i], dp[v])
  dp[i]+=1
    
for i in range(N):
  for v in range(i):
    if numbers[N-1-i] > numbers[N-1-v]:
      dp_inverse[N-1-i] = max(dp_inverse[N-1-i], dp_inverse[N-1-v])
  dp_inverse[N-1-i]+=1

result = 0

for i in range(N):
  result = max(result, dp[i] + dp_inverse[i])

print(result - 1)