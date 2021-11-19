# link : https://www.acmicpc.net/problem/9019
# Lv : gold 5
# Category : BFS

# BFS를 통해서 모든 경우의 수를 다 돌아본다. 이때 너비탐색을 해서 가장 먼저 도착점에 도달하는 것을 리턴하는 것으로 한다.
# 이때 중복하는 부분을 거치지 않기 위해서 visited를 통해서 관리하는 것이 시간관리의 핵심이다.

import sys  
from collections import deque

def calculate(mode, register):
  # D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
  if mode == 'D':
    if register*2 > 9999:
      return (register*2)%10000
    else:
      return register*2

  # S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
  elif mode == 'S':
    if register == 0:
      return 9999
    else:
      return register-1
  
  # L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
  elif mode == 'L':
    q, r =divmod(register, 1000)
    return q + r*10
  # R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
  elif mode == 'R':
    q, r =divmod(register, 10)
    return q + r*1000


# 테스트 케이스
T = int(sys.stdin.readline())
functions = ["D", "S", "L", "R"]
for i in range(T):
  A, B = map(int, sys.stdin.readline().split())
  visited = [[-1, ""] for i in range(10000)]
  queue = deque()
  queue.append(A)
  visited[A][0] = A
  while queue:
    num = queue.popleft() 
    if num == B:
      li = []
      while num != A:
        num, st = visited[num]
        li.append(st)

      answer = ""
      while li:
        answer += li.pop()
      print(answer)
      break
    
    for i in range(4):
      new_num = calculate(functions[i], num)
      if visited[new_num][0] == -1:
        visited[new_num][0] = num
        visited[new_num][1] = functions[i]
        queue.append(new_num)
