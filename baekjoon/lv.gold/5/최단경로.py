# link : https://www.acmicpc.net/problem/1753
# Lv : gold 5
# Category : 다익스트라, 우선순위 큐

# 이 문제는 경로마다 cost가 존재하고 cost를 최소화하는 경로를 찾는 문제입니다.
# 이렇게 경로가 있고 경로에 cost가 있다면 다익스트라 알고리즘 혹은 플루이드 워셜 알고리즘을 이용하죠!!
# 이 문제는 최종적으로 start 노드에서 다른 각 노드까지의 최단거리를 표현하면 되기 때문에 다익스트라 알고리즘을 활용했습니다.

from heapq import heappush, heappop

N, M = map(int,input().split())

start_node = int(input())

graph = { i : [] for i in range(1, N+1)}

for _ in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))


INF = int(1e9)

distance = [INF for _ in range(N+1)]

def dijkstra(start):
  distance[start] = 0
  queue = []
  queue.append([0, start])
  while queue:
    dist, node = heappop(queue)
    for destination, cost in graph[node]:
      if distance[destination] > dist + cost:
        distance[destination] = dist + cost
        heappush(queue, [dist + cost, destination])

dijkstra(start_node)

for i in range(1, N+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])