# link : https://www.acmicpc.net/problem/14502
# Lv : gold 5
# Category : 조합, BFS

# 우선 combinations 을 통해서 벽을 3개 세울 수 있는 모든 경우의 수를 구한 다음
# 반복문을 통해서 미리 벽을 세우고 bfs로 바이러스들이 전부다 퍼져나갔을 때 추가된 바이러스의 개수를 구합니다.
# 최종적으로 result에 들어 있는 각 경우의 추가된 바이러스 숫자 중에서 가장 작은 값을 추출하여 안전구역에서 빼주면 정답이 나옵니다.

from collections import deque
from itertools import combinations
from copy import deepcopy 

N, M = map(int,input().split())
graph = []
virus = []
can_wall = []
for i in range(N):
    graph.append(list(map(int,input().split())))

safe = -3
deq = deque()
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

result = float('inf')

for i in range(N):
  for v in range(M):
    if graph[i][v] == 2:
      virus.append([i, v])
    if graph[i][v] == 0:
      safe+=1
      can_wall.append([i, v])

comb = list(combinations(can_wall,3))


for tup in comb:
  graph_test = deepcopy(graph)
  for i, v in tup:
    graph_test[i][v] = 1
  deq = deque()
  visited = []
  virus_test = 0
  for i, v in virus:
    deq.append([i, v])
  while deq:
    r, c = deq.popleft()
    if [r, c] not in visited:
      for i in range(4):
        new_r, new_c = [r+ dy[i], c+ dx[i]]
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
          continue
        if graph_test[new_r][new_c] == 0:
          virus_test+= 1
          deq.append([new_r, new_c])
          graph_test[new_r][new_c] = 2
    visited.append([r, c])
  
  result = min(result, virus_test)

print(safe - result)