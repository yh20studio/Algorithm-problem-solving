# link : https://www.acmicpc.net/problem/1238
# Lv : gold 3
# Category : 다익스트라, 우선순위 큐

# 이 문제는 cost에 따른 최단 거리를 구하는 문제이다. 따라서 다익스트라 알고리즘을 사용하여 문제를 해결했다.
# 특이했던 점은 정해진 장소에 갔다가 다시 본인의 집으로 돌아와야 한다는 것이다.
# 따라서 갈때, 올때 모두 다익스트라를 활용하여 최소 cost로 이동해야한다. 

import sys
from heapq import heappush, heappop

N, M, X = map(int, (sys.stdin.readline().split()))
graph = {i : [] for i in range(1, N+1)}
graph_inverse = {i : [] for i in range(1, N+1)}

for i in range(M):
  start, end, cost = map(int, (sys.stdin.readline().split()))
  graph[start] += [(end, cost)]
  graph_inverse[end] += [(start, cost)]

INF = float('inf')
board = [INF for _ in range(N+1)]
que = []
que.append([0, X])
board[X] = 0

while que:
  cost, node = heappop(que)
  if board[node] < cost:
    continue
  for i, t in graph[node]:
    if board[i] > board[node] + t:
      board[i] = t + board[node]
      heappush(que, [board[i], i]) 

board_inverse = [INF for _ in range(N+1)]
que_inverse = []
que_inverse.append([0, X])
board_inverse[X] = 0

while que_inverse:
  cost, node = heappop(que_inverse)
  if board_inverse[node] < cost:
    continue
  for i, t in graph_inverse[node]:
    if board_inverse[i] > board_inverse[node] + t:
      board_inverse[i] = t + board_inverse[node]
      heappush(que_inverse, [board_inverse[i], i]) 

result = 0
for i in range(1, N+1):
  result = max(result, board[i] + board_inverse[i])

print(result)