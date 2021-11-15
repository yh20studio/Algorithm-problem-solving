# link : https://www.acmicpc.net/problem/13023
# Lv : gold 5
# Category : DFS

# 해당문제는 친구관계에서의 깊이를 구하는 과정이다. 따라서 DFS를 이용해서 깊이 우선 탐색을 해줘야한다.
# 이때 깊이가 5를 만족한다면 정답을 1로 출력한다.

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

# 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)
N, M = map(int, sys.stdin.readline().split())
global answer
answer = 0
friends = {i : [] for i in range(N)}

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  friends[a].append(b)
  friends[b].append(a)

def dfs(node, count):
  global answer
  if visited[node] == False:
    if count == 5: # DFS의 깊이가 5라면 주어진 조건을 만족한다.
      answer = 1
    else:
      for next_node in friends[node]:
        visited[node] = True
        dfs(next_node, count+1)
        visited[node] = False


for i in range(N): 
  visited = [False for _ in range(N)]
  dfs(i, 1)

print(answer)