# link : https://www.acmicpc.net/problem/1707
# Lv : gold 4
# Category : BFS

# 주어진 그래프들을 분할할 수 있는가?를 물어보는 문제이다. 
# 그래프들이 모두 연결되어있다는 보장이 없고, 조사해봐야할 그룹들이 여러개 있을 수 있다.
# 따라서 모든 노드에서 시작노드를 잡고, 연결된 노드 그래프에서 -1, 1로 체크를 하면서 분할한다.
# 이때 분할이 안되는 경우가 1개라도 생기면 answer = "NO"가 되는 것이다.

import sys
from collections import deque

K = int(sys.stdin.readline())

for _ in range(K):
  answer = "YES"
  V, E = map(int, sys.stdin.readline().split())
  graph = {i : [] for i in range(1, V+1)}
  graph_set = [0 for _ in range(V+1)]
  for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

  for i in range(1, V+1):
    queue = deque()
    # [시작 노드가 1, 각 노드간 집합 구분을 위해 -1, 0, 1을 사용]
    queue.append([i, -1]) 
    while queue:
      node, set_number = queue.popleft()
      if graph_set[node] == 0:
        for next_node in graph[node]:
          if set_number == -1:
            if graph_set[next_node] == -1:
              answer = "NO"
              break
            else:
              queue.append([next_node, 1])
          else:
            if graph_set[next_node] == 1:
              answer = "NO"
              break
            else:
              queue.append([next_node, -1])

        if answer == "NO":
            break
        graph_set[node] = set_number
    
    if answer == "NO":
        break

  print(answer)
