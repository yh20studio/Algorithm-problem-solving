# link : https://www.acmicpc.net/problem/12851
# Lv : gold 5
# Category : BFS, 구현

# 숨박꼭질 3 문제와는 달리 순간이동할 때 cost가 1초 증가하므로 큐를 이용해서 BFS를 했다.
# 이때 최소 cost로 도착하는 방법의 개수도 카운팅해야하므로 해당 location에 도착한다고 해도, break하지 않고
# 계속 찾아주는 방식을 사용했다.

import sys
from collections import deque

# N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
N, K = map(int, sys.stdin.readline().split())

# (0 ≤ N ≤ 100,000) 100001: 방문안함
visited = [100001 for _ in range(100001)]
answer = 0
count = 0
queue = deque()
queue.append([N, 0])

while queue:
  location, cost = queue.popleft()

  if location == K:
    answer = cost
    count += 1
  else:
    if (location-1) >= 0:
      if visited[location - 1] >= cost + 1:
        visited[location - 1] = cost + 1
        queue.append([location - 1, cost+1])
    
    if (location + 1) <= 100000:
      if visited[location + 1] >= cost + 1:
        visited[location + 1] = cost + 1
        queue.append([location + 1, cost+1])
    
    if location*2 <= 100000:
      if visited[location*2] >= cost+1:
        visited[location*2] = cost + 1
        queue.append([location*2, cost+1])

print(answer)
print(count)
