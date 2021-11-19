# link : https://programmers.co.kr/learn/courses/30/lessons/49191
# Lv : 3
# Category : BFS 

# 각 권투선수 간의 경기 결과가 들어있는 리스트가 있다.
# 이 리스트는 모든 선수들의 상하관계를 표현하지 않는다. 여러 스텝을 거쳐서 논리적인 추론이 가능한 관계가 있다는 것이다.
# 따라서 모든 선수들과 graph를 BFS로 돌면서 경기결과에 직접적으로 나오지 않는 상하관계를 모두 표시하기로 했다.
# 이 후 이 모든 표시관계에서 자신을 제외하고 선수들의 숫자만큼 나온다면 해당 선수는 순위를 표현할 수 있게 되는 것이다.

from collections import deque

def solution(n, results):
    answer = 0
    # 각 권투선수가 이긴 선수를 카운트 할 수 있도록 함
    graph = {i : [] for i in range(1, n+1)}
    
    for winner, loser in results:
        graph[winner].append(loser)
    
    queue = deque()
    
    # 모든 선수를 탐색하면서 선수들끼리의 상하관계를 모두 graph에서 나타낼 수 있도록 함
    for i in range(1, n+1):
        visited = []
        queue.append(i)
        while queue:
            winner = queue.popleft()
            if winner not in visited:
                for loser in graph[winner]:
                    queue.append(loser)
                        
                visited.append(winner)
        
        graph[i] = visited 
    
    
    cnt = [0 for i in range(n+1)]
    
    # graph를 돌면서 해당플레이어가 다른플레이어와의 순위 경쟁에 몇번 영향을 끼칠 수 있는 가를 카운트함
    for player, li in graph.items():
        cnt[player] += len(li)
        for loser in li:
            cnt[loser] += 1
    
    for i in range(1, n+1):
        if cnt[i] == n+1:
            answer+=1
            
    return answer