# link : https://www.acmicpc.net/problem/1197
# Lv : gold 4
# Category : MST, 프림 알고리즘

# 프림 알고리즘(노드 선택을 기반)
# 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장 해나가는 방법
# 이전 단계에서 만들어진 신장 트리를 확장하는 방법이다. -> 노드를 기반으로 선택
# 1. 시작 단계에서는 시작 노드만이 MST 집합에 포함된다.
# 2. 앞 단계에서 만들어진 MST 집합에 인접한 노드들 중에서 최소 간선으로 연결된 노드을 선택하여 트리를 확장한다.
# 3. 위의 과정을 노드들이 모두 연결될 때까지 진행한다.

import sys
from heapq import heappop, heappush

V, E = map(int, sys.stdin.readline().split())

def solve():
  connected  = [] 
  graph = {i : [] for i in range(1, V+1)}
  answer = 0
  for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])
  
  connected.append(1)
  queue = []
  for node, cost in graph[1]:
    heappush(queue, [cost, node])
  
  while queue:
    cost, node = heappop(queue)
    if node not in connected:
      answer+= cost
      for n, c in graph[node]:
        heappush(queue, [c, n])
        
      connected.append(node)
  
  print(answer)  

solve()