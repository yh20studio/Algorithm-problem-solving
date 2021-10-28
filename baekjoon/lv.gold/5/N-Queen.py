# link : https://www.acmicpc.net/problem/9663
# Lv : gold 5
# Category : 백트레킹

# 문제는 백트래킹을 사용하여 푸는 문제다.
# 가능한 모든 경로를 찾아봐야하지만 일반적인 dfs로 푼다면 시간초과가 되기 때문에
# 중간 중간 확인을 하면서 문제와 맞지 않는 경우들은 모든 경로를 찾을 때 포함되지 않도록 하는 것이다.

n = int(input())

result = 0

def check(visitied, depth):
  global result 
  for number in range(n):
    if number in visitied:
      continue
    if find_queen(visitied, depth, number):
      if depth == n-1 :
        result+=1
      else:
        visitied[depth] = number
        check(visitied, depth+1)
        visitied[depth] = -1
        
def find_queen(visitied, depth, queen_row): 
  for v in range(depth):
    if abs(visitied[v] - queen_row) == abs(v - depth):
      return False
  return True       


for i in range(n):
  visitied = [-1 for _ in range(n)]
  visitied[0] = i
  check(visitied, 1)

if n == 1:
  result = 1
  
print(result) 