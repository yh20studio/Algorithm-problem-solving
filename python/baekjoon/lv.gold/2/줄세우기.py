# https://www.acmicpc.net/problem/2252
# Lv : gold 2
# Category : 위상정렬

# 진입차수가 0인 노드부터 순서대로 알고리즘을 따라가는데 다음과 같다.
# 해당 노드에서 부터 연결된 간선을 모두 제거한다.
# 만약 간선이 제거되면서 진입 차수가 0이 된 노드가 있다면 해당 노드를 큐에 넣어준다.
# 큐가 끝날때 까지 이를 반복한다.
# 이때 위상정렬은 진입차수가 0인 노드가 여러개라면 어떤 노드를 먼저 큐에 넣고 실행하는가에 따라서 순서의 결과가 달라질 수 있다는 점을 유의해야한다.

import sys
from collections import deque

def makeLine():
  for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    degree[end] += 1

def order():
  startList = []
  for i in range(1, N+1):
    if degree[i] == 0:
      startList.append(i)

  queue = deque()
  queue.extend(startList)
  while queue:
    node = queue.popleft()    
    if f"{node}" not in visited:
      for end in graph[node]:
        degree[end] -= 1
        if degree[end] == 0:
          queue.append(end)

      visited.append(f"{node}")

N, M = map(int, sys.stdin.readline().split())

graph = {i : [] for i in range(1, N+1)}
degree = [0 for _ in range(N+1)]
visited = []

makeLine()
order()

print(" ".join(visited))