# link : https://www.acmicpc.net/problem/1766
# Lv : gold
# Category : 우선순위 큐, 구현

# 한 문제집을 풀어야하는데 선행해야하는 문제집이 있으므로, 해당 조건을 그래프와 리스트로 나타낸 후 모든 선행 조건이 맞았을 때만 
# 우선순위 큐에 넣는 방식으로 해결했습니다.

import sys  
from heapq import heappush, heappop

N, M = map(int, (sys.stdin.readline().split()))
queue = []
graph = {i : [] for i in range(1, N+1)}
condition = [[] for i in range(N+1)]
answer = []

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  condition[b].append(a)
  graph[a].append(b)

for i in range(1, N+1):
  if len(condition[i]) == 0:
    heappush(queue, i)

while queue:
  book = heappop(queue)
  for next_book in graph[book]:
    condition[next_book].remove(book)
    if len(condition[next_book]) == 0:
      heappush(queue, next_book)
  answer.append(f"{book}")

print(" ".join(answer))  