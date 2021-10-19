# link : https://www.acmicpc.net/problem/1202
# Lv : gold
# Category : 우선순위 큐

# 보석을 가방에 한개씩만 담을 수 있으므로 매 가방마다 넣을 수 있는 보석 리스트에서 
# 가장 비싼 값을 가지는 보석을 넣어주는 방식으로 진행한다.

# 가방의 용량을 작은 순으로 나열하기 위하여 우선순위 큐 사용
# 가능한 보석을 찾기 위하여 보석의 무게가 작은순으로 우선순위 큐 사용
# 가능한 보석에서 가장 비싼 보석을 찾기 위하여 우선순위 큐 사용

import sys  
from heapq import heappush, heappop

answer = 0 
# 보석의 갯수, 가방의 갯수
N, K = map(int, (sys.stdin.readline().split()))
gem_ordered_weight = []
capabel_gems = []
bags = []

for i in range(N):
  M, V = map(int, (sys.stdin.readline().split()))
  heappush(gem_ordered_weight, [M, V])
  
# 가방의 담을 수 있는 최대 무게를 기준으로 우선순위 큐 만들기
for i in range(K):
  C = int(sys.stdin.readline())
  heappush(bags, C)

while bags:
  remain = heappop(bags)

  # 가방의 용량보다 작은 보석들을 꺼내어 가격 순으로 다시 우선순위 큐에 넣음
  while gem_ordered_weight and gem_ordered_weight[0][0] <= remain: 
    m, v = heappop(gem_ordered_weight)
    heappush(capabel_gems, -v)
  
  # 매 가방마다 넣을 수 있는 보석 중에서 가장 가격이 비싼 보석으로 넣는다.
  if len(capabel_gems) > 0:
    answer -= heappop(capabel_gems)
  else:
    if len(gem_ordered_weight) == 0:
      break
    
print(answer)