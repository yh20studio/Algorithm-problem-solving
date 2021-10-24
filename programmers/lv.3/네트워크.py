# link : https://programmers.co.kr/learn/courses/30/lessons/43162
# Lv : 3
# Category : BFS

# 파이썬을 활용했고 노드들끼리 연결된 네트워크를 찾고 개수를 카운팅 하기 위해서 BFS 알고리즘을 이용했습니다. 
# 알고리즘을 이용하면서 Queue를 활용하기 위해서 deque를 import해서 이용 했고 연결되어 있는 노드들을 찾고 해당 노드들을 그래프에서 제거하고 answer의 값을 늘려가는 방법을 사용했습니다.

from collections import deque

def solution(n, computers):
    answer = 0
    graph = {}
    for i, li in enumerate(computers):
        graph[i] = li
    
    for j in range(n):
        if j in graph:
            li = BFS_with_adj_list(graph, j)
            for m in li:
                graph.pop(m)
            answer += 1
    
    return answer


def BFS_with_adj_list(graph, key):
    visited = []
    queue = deque([key])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            for i, v in enumerate(graph[n]):
                if v == 1:
                    queue.append(i)
                    
    return visited