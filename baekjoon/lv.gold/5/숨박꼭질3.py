# link : https://www.acmicpc.net/problem/13549
# Lv : gold 5
# Category : 우선순위 큐

# BFS를 이용하여 순차적인 탐색을 하려고 했지만, 순간이동을 하면 걸리는 시간 초가 0초이므로 순간이동을 고려하면
# 순차적인 탐색이 힘들것이라 생각했다. 따라서 우선순위 큐를 활용하여 시간이 적게 걸렸던 순으로 탐색을 하도록 했다.

import sys
from heapq import heappop, heappush

# N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
N, K = map(int, sys.stdin.readline().split())

# (0 ≤ N ≤ 100,000) 100001: 방문안함
visited = [100001 for _ in range(100001)]
answer = 0

queue = []
heappush(queue, [0, N])

while queue:
  cost, location = heappop(queue)

  if location == K:
    answer = cost
    break
  if (location-1) >= 0:
    if visited[location - 1] > cost + 1:
      visited[location - 1] = cost + 1
      heappush(queue, [cost+1, location - 1])
  
  if (location + 1) <= 100000:
    if visited[location + 1] > cost + 1:
      visited[location + 1] = cost + 1
      heappush(queue, [cost+1, location + 1])
  
  if location*2 <= 100000:
    if visited[location*2] > cost:
      visited[location*2] = cost
      heappush(queue, [cost, location*2])

print(answer)