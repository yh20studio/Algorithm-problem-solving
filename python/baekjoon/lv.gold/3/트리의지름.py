# link : https://www.acmicpc.net/problem/1167
# Lv : gold 3
# Category : DFS, 트리

# 이 문제는 트리가 주어지고 각 트리를 연결하는 간선의 가중치가 있는 모습이다.
# 시간초과에 대한 문제를 해결하기 위해서 사용한 방법은 최대값이 나올만한 노드를 미리 찾아서 해당 노드만 탐색을 진행하는 방법이다. 
# 트리의 노드들은 모두 연결이 되어있으며 한 노드에서 다른 노드까지의 가중치의 합을 구해서 비교해보면 최대값이 나올 수 있는 노드를 구할 수 있다.
# 👉 여기서 한 노드만을 통해서 구한 최대값을 그대로 사용하면 되지 않는가? 라는 의문이 떠오를 수 있지만, 만약 해당 노드의 부모노드가 존재하게 된다면 이 값은 최종적인 답이 될 수 없다.
# 따라서 findMaxIndex를 통해서 dfs 탐색을 할 노드를 찾고 탐색을 진행해주면 된다.

import sys

answer = 0
N = int(sys.stdin.readline())
tree = {i : [] for i in range(1, N+1)}
check = [-1]*(N+1)

for i in range(N):
  li = list(map(int, sys.stdin.readline().split()))
  root = li[0]
  li.pop()
  while len(li) > 1:
    dist = li.pop()
    node = li.pop() 
    tree[root].append((node, dist))


def findMaxIndex(node, check):
  for destination, dist in tree[node]:
    if check[destination] == -1:
      check[destination] = check[node] + dist  
      findMaxIndex(destination, check)

def dfs(node, r, visited):
  global answer
  for destination, dist in tree[node]:
    if destination not in visited:
      visited.add(node)
      dfs(destination, r+dist, visited)
      visited.remove(node)
    else:
      answer = max(answer, r)
    

findMaxIndex(1, check)
dist = 0
startNode = 1 
for i in range(1, N+1):
  if dist < check[i]:
    dist = check[i]
    startNode = i


dfs(startNode, 0, set())

print(answer)