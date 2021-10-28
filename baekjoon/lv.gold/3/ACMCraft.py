# link : https://www.acmicpc.net/problem/1005
# Lv : gold 3
# Category : 위상정렬

# 위상정렬 : 그래프가 주어지고 순서가 정해져 있는 작업을 차례로 수행해야 할 때, 순서를 결정할 때 사용하는 알고리즘이다. 하나의 방향 그래프에는 여러 개의 위상 정렬이 가능하다.

import sys
from collections import deque

T = int(sys.stdin.readline())
result = []

for i in range(T):
  N, K = map(int, (sys.stdin.readline().split()))
  D = list(map(int, sys.stdin.readline().split()))
  graph = {i : [] for i in range(1, N+1)}
  
  indegree =[0 for _ in range(N)]
  for j in range(K):
    start, end = map(int, sys.stdin.readline().split())
    graph[start] += [end]
    indegree[end-1] += 1
  
  deq = deque()
  order = []

  for v in range(N):
    if indegree[v] == 0:
      deq.append(v+1)

  while deq:
    node = deq.popleft()
    
    for number in graph[node]:
      indegree[number-1] -= 1
      if indegree[number-1] == 0:
        deq.append(number)

    order.append(node)
    
  W = int(sys.stdin.readline())

  board = [0 for _ in range(N+1)]
  complete = []
  
  for start in order:
    board[start] = board[start] + D[start-1]   
    
    for end in graph[start]:
      board[end] = max(board[end], board[start])   
  
  result.append(board[W])

for number in result:
  print(number)