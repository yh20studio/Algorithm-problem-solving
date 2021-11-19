# https://programmers.co.kr/learn/courses/30/lessons/86971
# Weekly Challenge
# Category : 탐색, 구현

# 상대적으로 주어지는 INPUT의 개수가 낮으므로 모든 간선에서 노드의 개수 차이를 계산해보고 비교해보는 방식을 사용했다.

def countNode(graph, a, b):
    stack = [a]
    node_cnt = 1
    visited = [a]
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if next_node != b and next_node not in visited:
                node_cnt+= 1
                stack.append(next_node)
        visited.append(node)
    
    return len(visited)

def solution(n, wires):
    answer = 101
    graph = {i : [] for i in range(1, n+1)}
    
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    for start, end in wires:
        answer = min(answer, abs(countNode(graph, start, end) - countNode(graph, end, start)))
        
    
    return answer