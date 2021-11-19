# link : https://www.acmicpc.net/problem/1916
# Lv : gold 5
# Category : 다익스트라, 우선순위 큐

# 도시간의 버스를 타고 이동하는데, 이 버스마다 cost가 존재하고 다 다른 문제이다.
# 이렇게 cost가 존재할 때는 다익스트라 알고리즘을 활용하여 문제를 접근
# 이때 일반 큐를 사용하지 않고 우선순위 큐를 사용하는 이유는 
# 일반 큐를 사용하면 가능한 경우의 수를 모두 살펴보면서 최소 거리를 찾는 것이다 -> O(N)
# 우선순위 쿠를 사용하면 가장 작은 cost를 먼저 살펴볼 수 있기 때문에 훨씬 빠르다. -> O(log(N))

import sys  
from heapq import heappop, heappush

answer = 0
N = int(sys.stdin.readline()) # 도시의 개수 N(1 ≤ N ≤ 1,000)
M = int(sys.stdin.readline()) # 버스의 개수 M(1 ≤ M ≤ 100,000)

graph = {i : [] for i in range(1, N+1)}

for _ in range(M):
  s, e, cost = map(int, sys.stdin.readline().split())
  graph[s].append([e, cost])

start, end = map(int, sys.stdin.readline().split())

# start로 부터 다른 도시까지의 cost
distance = [float('inf') for i in range(N+1)]
distance[start] = 0
queue = []
heappush(queue, [distance[start], start])

while queue:
  c, node = heappop(queue)
  if node == end:
    answer = c
    break
  for e, cost in graph[node]:
    if distance[node] + cost < distance[e]:
      distance[e] = distance[node] + cost
      heappush(queue, [distance[e], e])
      
print(answer)
