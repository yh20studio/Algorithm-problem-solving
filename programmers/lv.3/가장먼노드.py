# link : https://programmers.co.kr/learn/courses/30/lessons/49189
# Lv : 3
# Category : 다익스트라, 우선순위 큐

# 시작 노드인 1로 부터 가장 먼 노드들을 찾는 것이다. 각 노드들 마다 cost가 존재하지는 않지만
# 각 노드들의 cost를 1이라고 가정하고, 다익스트라를 이용하여 해결했다.

from heapq import heappush, heappop

def solution(n, edge):
    answer = 0
    graph = {i : [] for i in range(1, n+1)}
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    distance = [float('inf') for i in range(n+1)] # 1로 부터 간선의 갯수
    queue = []
    distance[0] = 0
    distance[1] = 0
    heappush(queue, [distance[1], 1])
    
    while queue:
        d, node = heappop(queue)
        for end in graph[node]:
            if distance[end] > d + 1 :
                distance[end] = d + 1
                heappush(queue, [d+1, end])
    
    max_distance = max(distance)

    for i in range(1, n+1):
        if distance[i] == max_distance:
            answer += 1
    
    return answer