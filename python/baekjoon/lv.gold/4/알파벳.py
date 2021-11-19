# link : https://www.acmicpc.net/problem/1987
# Lv : gold 4
# Category : DFS

# 이 문제가 복잡하다고는 느끼지 않지만 시간초과에 걸리지 않게 하기 위해 많이 노력을 했습니다
# 파이썬의 모듈 copy.deepcopy 가 있습니다.
# 리스트가 공유되지 않도록 깊은 복사를 하는 것인데 이게 시간이 매우 오래걸린다는 사실을 알았습니다. 
# 그동안에는 깊은 복사가 필요할 때마다 deepcopy를 이용했는데 이 모듈보다 슬라이싱을 하는게 훨씬 빠르다고 합니다.

N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]
board = [[False for _ in range(M)] for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

result = 0

def dfs(r, c, visit, alphabet):
  global result
  count = 0
  alphabet_set = set(visit)
  if board[r][c] != alphabet_set:
    board[r][c] = alphabet_set
    visit.append(graph[r][c])
    for i in range(4):
      new_r = r + dy[i]
      new_c = c + dx[i]
      if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
        continue
      if graph[new_r][new_c] not in visit:
        count += 1
        li = visit[:]
        dfs(new_r, new_c, li, alphabet+1)
  if count == 0:  
    result = max(result, alphabet)

dfs(0, 0, [], 1)
print(result)