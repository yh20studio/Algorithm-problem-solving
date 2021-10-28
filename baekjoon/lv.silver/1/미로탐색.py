# link : https://www.acmicpc.net/problem/2178
# Lv : silver 1
# Category : BFS

# 각 4방향으로 갈 수 있다고 가정한 상태로 bfs를 통한 완전탐색으로 문제를 풀이했습니다. 
# 탐색과정에서 이미 들렀던 곳은 다시 방문하는 일을 방지 했으며, 마지막 도착지점에 도착시에 가장 작은 값이 출력될 수 있도록 코드를 짰습니다.
# 시간 복잡도에서 높아질 수 있는 경우가 많으므로 주의를 하며 풀었고, 방문한 좌표를 다시 방문하지 않게 하는 것이 포인트 였습니다.
# 여기서 마지막 도착치를 제외하고는 방문한 좌표를 다시 방문할 때 count의 숫자가 줄어들 일이 없다는 것을 기본적인 바탕으로 생각하고 풀었습니다.

from collections import deque
n, m = map(int,input().split())

board = list()
ans = 0

for _ in range(n):
    board.append(list(map(int,input())))

dy = [1, 0, -1, 0]
dx = [0, 1, -0, -1]
deq = deque()
deq.append([0,0,1])
visited = [[False for _ in range(m)] for _ in range(n)]
while deq:
  location = deq.popleft()
  for i in range(4):
    y, x, count = location 
    y += dy[i]
    x += dx[i]
    if y < 0 or y > n-1 or x < 0 or x > m-1:
      continue
    if visited[y][x] == True:
      continue
    if board[y][x] != 0:
      if board[y][x] == 1:
        count+= 1
        board[y][x] = count
        if y == n -1 and x ==  m-1:
          pass
        else:
          deq.append([y, x, count])
          visited[y][x] = True
      else:
        if count < board[y][x]:
          count+= 1
          board[y][x] = count
          if y == n -1 and x ==  m-1:
            pass
          else:
            deq.append([y, x, count])
            visited[y][x] = True

print(board[n-1][m-1])