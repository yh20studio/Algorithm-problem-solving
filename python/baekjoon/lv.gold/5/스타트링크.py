# link : https://www.acmicpc.net/problem/5014
# Lv : gold 5
# Category : BFS

# visited를 통해서 각 층수에 도달했는지를 판단하면서 BFS로 탐색하게되면, 원하는 층수에 도달할 수 있는지 알게된다.

import sys  
from collections import deque
    
answer = 0
# F: 건물 층수, S: 현재 층수, G: 스타트링크 층수, U: 위로 이동 층수, D: 아래로 이동 층수
F, S, G, U, D = map(int, sys.stdin.readline().split())

visited = [0 for i in range(F+1)]
queue = deque()
queue.append([S, 0])
answer = "use the stairs"

while queue:
  now, count = queue.popleft()
  if now == G:
    answer = count
    break

  if visited[now] == 0: # 방문하지 않았더라면
    if now + U <= F:
      queue.append([now+U, count+1])
    if 0 < now - D:
      queue.append([now-D, count+1])
    
    visited[now] = 1

print(answer)