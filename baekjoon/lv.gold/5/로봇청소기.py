# link : https://www.acmicpc.net/problem/14503
# Lv : gold 5
# Category : 구현

# 로봇 청소기는 처음에 자신의 시작 구역을 청소한다
# 로봇 청소기는 왼쪽으로 돌면서 청소할 곳이 있는지 살펴본다.
# 청소할 곳을 발견한 즉시 그 지역으로 간다.
# 만약 한바퀴를 다 돌았는데 청소할 구역이 없다면 현재 방향을 유지하고 한칸 후진한다.
# 이때 만약 뒤에 벽이 있어서 후진할 곳이 없다면 그대로 로봇 청소기는 종료된다.


N, M = map(int, input().split())
r, c, d = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
direction = [3, 0, 1, 2]
board = []
for i in range(N):
  board.append(list(map(int, input().split())))

def check(location, r, c, d):
  new_d = direction[d]
  new_r = r + dy[new_d]
  new_c = c + dx[new_d]
  if board[new_r][new_c] == 0:
    board[new_r][new_c] = 2
    location.append([new_r, new_c, new_d])
    return True
  return False

def fresh(board, r, c, d):
  location = [[r, c, d]] 
  board[r][c] = 2
  count = 1
  while location:
    r, c, d = location.pop()
    can_fresh = False
    for i in range(4):
      if check(location, r, c, d):
        count+=1
        can_fresh = True
        break
      else:
        d = direction[d]
    if can_fresh == False:
      if board[r- dy[d]][c-dx[d]] != 1:
        location.append([r - dy[d], c  - dx[d], d])

  return count

print(fresh(board, r, c, d))