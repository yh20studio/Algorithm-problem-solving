# link : https://www.acmicpc.net/problem/14500
# Lv : gold 5
# Category : 구현

# 이 문제는 각 모양의 회전과 대칭을 모두 고려하여 최종합의 최댓값을 측정해야합니다.
# 그렇기에 각 모양의 대한 회전 및 대칭을 모두 구현을 해야합니다.
# 각 경우를 모양으로 나누고 모두 조건문과 반목문을 통해서 구현했습니다.

import sys

def shape_stick(r, c):
  score = 0
  # 정방향
  if c+3 < M:
    count = 0
    for i in range(4):
      count += board[r][c+i]
    score = max(score, count)
  # 회전
  if r+3 < N:
    count = 0
    for i in range(4):
      count += board[r+i][c]
    score = max(score, count)
  
  return score

def shape_squre(r, c):
  score = 0
  # 정방향
  if c+1 < M and r+1 < N:
    for i in range(2):
      for v in range(2):
        score += board[r+i][c+v]
  return score

def shape_L(r, c):
  score = 0
  # 정방향
  if r+2 < N and c+1 < M:
    count = 0
    for i in range(3):
      count += board[r+i][c]
    count += board[r+2][c+1]  
    score = max(score, count)
  # 90도 회전
  if r+1 < N and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r][c+i]
    count += board[r+1][c]
    score = max(score, count)
  # 180도 회전
  if r+2 < N and c+1 < M:
    count = 0
    for i in range(3):
      count += board[r+i][c+1]
    count += board[r][c]
    score = max(score, count)
  # 270도 회전
  if 0 <= r-1 and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r][c+i]
    count += board[r-1][c+2]
    score = max(score, count)
  
  # 대칭
  if r+2 < N and c-1 >= 0:
    count = 0
    for i in range(3):
      count += board[r+i][c]
    count += board[r+2][c-1]  
    score = max(score, count)
  
  # 대칭, 90도 회전
  if r+1 < N and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r+1][c+i]
    count += board[r][c]  
    score = max(score, count)
  
  # 대칭, 180도 회전
  if r+2 < N and c+1 < M:
    count = 0
    for i in range(3):
      count += board[r+i][c]
    count += board[r][c+1]  
    score = max(score, count)
  
  # 대칭, 270도 회전
  if r+1 < N and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r][c+i]
    count += board[r+1][c+2]  
    score = max(score, count)

  return score

def shape_lightning(r, c):
  score = 0
  # 정방향
  if r+2 < N and c+1 < M:
    count = 0
    for i in range(2):
      count += board[r+1][c+i]
    count += board[r][c]  
    count += board[r+2][c+1]  
    score = max(score, count)
  # 90도 회전
  if 0 <= r-1 and c+2 < M:
    count = 0
    for i in range(2):
      count += board[r-1+i][c+1]
    count += board[r][c]  
    count += board[r-1][c+2]  
    score = max(score, count)
  # 대칭
  if 0 <= r-2 and c+1 < M:
    count = 0
    for i in range(2):
      count += board[r-1][c+i]
    count += board[r][c]  
    count += board[r-2][c+1]  
    score = max(score, count)
  # 대칭 90도 회전
  if r+1 < N and c+2 < M:
    count = 0
    for i in range(2):
      count += board[r+i][c+1]
    count += board[r][c]  
    count += board[r+1][c+2]  
    score = max(score, count)

  return score

def shape_last(r, c):
  score = 0
  # 정방향
  if r+1 < N and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r][c+i]
    count += board[r+1][c+1]    
    score = max(score, count)
  # 90도 회전
  if r+2 < N and 0 <= c-1:
    count = 0
    for i in range(3):
      count += board[r+i][c]
    count += board[r+1][c-1]    
    score = max(score, count)
  # 180도 회전
  if 0 <= r-1 and c+2 < M:
    count = 0
    for i in range(3):
      count += board[r][c+i]
    count += board[r-1][c+1]    
    score = max(score, count)
  # 270도 회전
  if r+2 < N and c+1 < M:
    count = 0
    for i in range(3):
      count += board[r+i][c]
    count += board[r+1][c+1]    
    score = max(score, count)
  
  return score


N, M = map(int, sys.stdin.readline().split())
board = []

for i in range(N):
  board.append(list(map(int, sys.stdin.readline().split())))
  
result = 0
for i in range(N):
  for j in range(M):
    result = max(result, shape_stick(i, j))
    result = max(result, shape_squre(i, j))
    result = max(result, shape_L(i, j))
    result = max(result, shape_lightning(i, j))
    result = max(result, shape_last(i, j))
  
print(result)