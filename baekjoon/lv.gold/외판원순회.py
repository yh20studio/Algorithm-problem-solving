# link : https://www.acmicpc.net/problem/2098
# Lv : gold
# Category : 다이나믹프로그래밍, 비트마스킹

import sys

def dfs(node, route):
  if dp[node][route] != 0:
    return dp[node][route]
  if route == (1 << N) - 1:
    if mat[node][0] != 0:
      return mat[node][0]
    else:
      return float('inf')

  else:
    tmp = float('inf')
    for end in graph[node]:
      if route & (1 << (end)):
        continue
      tmp = min(tmp, dfs(end, route|(1 << end)) + mat[node][end])
    dp[node][route] = tmp
  
  return tmp
    
N = int(sys.stdin.readline())
mat = []
graph = {i : [] for i in range(N)}
dp = [[0 for _ in range(2**N)] for _ in range(N)]
for i in range(N):
  li = list(map(int, (sys.stdin.readline().split())))
  mat.append(li)
  for x in range(N):
    if li[x]!=0:
      graph[i].append(x)

print(dfs(0, 1))

