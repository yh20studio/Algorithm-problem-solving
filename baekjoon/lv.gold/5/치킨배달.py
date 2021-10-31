# link : https://www.acmicpc.net/problem/15686
# Lv : gold 5
# Category : 조합

# 어느 치킨집을 고르는가에 따라서 각 거리의 합이 계속 달라지기 때문에 모든 경우의 수를 탐색하고 최솟값을 탐색하기로 했습니다.
# 주어진 남겨야할 치킨집 개수를 이용하여 가능한 조합 경우의 수를 구했습니다.

import sys
from itertools import combinations

def minimumChickenDistance():
  chicken_comb = list(combinations(chickens, M))
  answer = float('inf')
  for selected_chickens in chicken_comb:
    dist_sum = 0
    chicken_dist = [[0 for _ in range(N)] for _ in range(N)]
    for chicken in selected_chickens:
      chicken_r, chicken_c = chicken
      for house_r, house_c in house:
        dist = abs(chicken_r - house_r) + abs(chicken_c - house_c)
        if chicken_dist[house_r][house_c] == 0:
          dist_sum += dist
          chicken_dist[house_r][house_c] = dist
        elif chicken_dist[house_r][house_c] > dist:
          dist_sum -= chicken_dist[house_r][house_c]
          dist_sum += dist
          chicken_dist[house_r][house_c] = dist
    answer = min(answer, dist_sum)  

  return answer

N, M = map(int, sys.stdin.readline().split())
town = [[0 for _ in range(N)] for _ in range(N)]

chickens = []
house = []

for r in range(N):
  li = list(map(int, sys.stdin.readline().split()))
  for c in range(N):  
    if li[c] == 1:
      town[r][c] = 1
      house.append((r, c))
    elif li[c] == 2:
      town[r][c] = 2
      chickens.append((r, c))

print(minimumChickenDistance())