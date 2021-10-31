# link : https://www.acmicpc.net/problem/10942
# Lv : gold 3
# Category : 다이나믹프로그래밍


# palindrome : 회문 또는 팰린드롬은 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열 등이다. 
# 보통 낱말 사이에 있는 띄어쓰기나 문장 부호는 무시한다.

# 여기서 펠린드롬을 증명하기 위해서는 각 S, E에서 한 칸씩 이동한 S+1, E-1 또한 펠린드롬을 이루어야 한다. 
# 이를 바탕으로 다이나믹 프로그래밍 알고리즘을 이용하여 문제를 해결하면 쉽다.
# 이때 펠린드롬을 구하기 위해서 이전에 했던 계산이 있다면.. Check 이중 배열을 통해서 펠린드롬이 가능한지 확인하고 가능하다면 계산을 더 하지 않고 1을 반환하도록 했다.

import sys

def palindrome(S, E):

  if check[S][E] == 1:
    return 1
  
  if S == E:
    return 1
  if E - S == 1:
    if numbers[S] == numbers[E]:
      check[S][E] = 1
      return 1
    else:
      return 0 
  
  if palindrome(S+1, E-1) == 1:
    if numbers[S] == numbers[E]:
      check[S][E] = 1
      return 1
    else:
      return 0
  else:
    return 0

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
questions = []

check = [[0 for _ in range(N)] for _ in range(N)]

for i in range(M):
  questions.append(list(map(int, sys.stdin.readline().split())))

for S, E in questions:
  print(palindrome(S-1, E-1))