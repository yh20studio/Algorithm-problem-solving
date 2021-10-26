# link : https://www.acmicpc.net/problem/14891
# Lv : gold 5
# Category : 구현

# 기어가 돌아감에 따라서 옆에 있는 기어도 영향을 끼치는 문제이다.
# 따라서 한번 돌아갈때마다 모든 기어에 대해서 if문을 통해서 확인 하고, 회전시켜주는 것이 중요하다.
# 이때 모든 기어의 값을 추적하면 시간과 메모리가 많이 드니, 기어의 12시 방향 부분의 index만 추적하는것으로 해결했다.

import sys  

def findGearRigth(gear): # 기어의 오른쪽 맞닿은 부분 찾기
  if gears_start[gear] >5:
    return 2+ gears_start[gear] - 8
  else: 
    return 2+ gears_start[gear]

def findGearLeft(gear): # 기어의 왼쪽 맞닿은 부분 찾기
  if gears_start[gear] > 1:
    return 6+ gears_start[gear] - 8
  else: 
    return 6+ gears_start[gear]

def rotateGear(gear, direction): # 기어 회전
  gears_start[gear] -= direction
  if gears_start[gear] == 8:
    gears_start[gear] = 0
  elif gears_start[gear] == -1:
    gears_start[gear] = 7

gears = [[]]
gears_start = [-1, 0, 0, 0, 0]
# 12시방향부터 시계방향 순서대로 주어진다. N극은 0, S극은 1로 나타나있다.
# 서로 맞닿은 부분은 index로 오른쪽 : 2, 왼쪽 : 6 
for i in range(4):
  gears.append(list(map(int, list(str(sys.stdin.readline()))[:-1])))

#  K (1 ≤ K ≤ 100) 총 회전 횟수
K = int(sys.stdin.readline())

# 방향이 1인 경우는 시계 방향이고, -1인 경우는 반시계 방향이다.
for _ in range(K):
  gear, direction = map(int, sys.stdin.readline().split())
  
  gear_1_right = gears[1][findGearRigth(1)] # 1번 기어의 오른쪽 맞닿은 부분
  gear_2_left = gears[2][findGearLeft(2)] # 2번 기어의 왼쪽 맞닿은 부분
  gear_2_right = gears[2][findGearRigth(2)] # 2번 기어의 오른쪽 맞닿은 부분
  gear_3_left = gears[3][findGearLeft(3)] # 2번 기어의 왼쪽 맞닿은 부분
  gear_3_right = gears[3][findGearRigth(3)] # 2번 기어의 오른쪽 맞닿은 부분
  gear_4_left = gears[4][findGearLeft(4)] # 2번 기어의 왼쪽 맞닿은 부분

  rotateGear(gear, direction) # 선택된 기어 회전

  if gear == 1:
    if gear_1_right != gear_2_left: # 2 기어 회전
      rotateGear(2, -direction)
      if gear_2_right != gear_3_left: # 3 기어 회전
        rotateGear(3, direction)
        if gear_3_right != gear_4_left: # 4 기어 회전
          rotateGear(4, -direction)

  elif gear == 2:
    if gear_1_right != gear_2_left:  # 1 기어 회전
      rotateGear(1, -direction)
    if gear_2_right != gear_3_left: # 3 기어 회전
      rotateGear(3, -direction)
      if gear_3_right != gear_4_left: # 4 기어 회전
        rotateGear(4, direction)

  elif gear == 3:
    if gear_2_right != gear_3_left: # 2 기어 회전
      rotateGear(2, -direction)
      if gear_1_right != gear_2_left:  # 1 기어 회전
        rotateGear(1, direction)
    if gear_3_right != gear_4_left: # 4 기어 회전
      rotateGear(4, -direction)
  
  elif gear == 4:
    if gear_3_right != gear_4_left: # 3 기어 회전
      rotateGear(3, -direction)
      if gear_2_right != gear_3_left: # 2 기어 회전
        rotateGear(2, direction)
        if gear_1_right != gear_2_left:  # 1 기어 회전
          rotateGear(1, -direction)

# 점수 내기
answer = 0
for i in range(1, 5):
  gear = gears[i]
  if gear[gears_start[i]] == 1:
    answer+= 2**(i-1)

print(answer)