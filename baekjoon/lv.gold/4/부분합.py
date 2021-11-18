# link : https://www.acmicpc.net/problem/1806
# Lv : gold 4
# Category : 투 포인터

# 연속된 수열의 부분합을 탐색하면서 조건과 맞을 때 최소 길이를 구하는 것이다. 
# 주어진 수열이 있고, 순서가 변하지 않으므로 투 포인터를 이용해서 순차적으로 탐색한다.

import sys

answer = 100001 # 최장 수열의 길이는 100000
N, S = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum_of_numbers = numbers[start]

while start <= end:
  if sum_of_numbers < S:
    if end == N-1:
      break
    else:
      end += 1
      sum_of_numbers += numbers[end]
  else:
    answer = min(answer, end-start+1)
    sum_of_numbers -= numbers[start]
    start += 1
    
if answer == 100001:
  print(0)
else:
  print(answer)