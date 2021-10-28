# link : https://www.acmicpc.net/problem/9251
# Lv : gold 5
# Category : LCS 알고리즘

# 이 문제는 LCS 알고리즘을 활용하여 푸는 문제이다. 
# LCS는 다이나믹 프로그래밍 알고리즘으로부터 기인하는데 중간 계산을 저장하는 방식이다.
# 각 알파벳을 하나씩 비교하면서 비교한 값을 저장하는 방식이다. 
# 다음 알파벳을 계산할 때에는 여태까지 적용된 알파벳에 대한 값을 dp 테이블에서 꺼내와 현재 알파벳과 비교값을 더해주는 것이다.

first = list(input())
second = list(input())

def lcs(first, second):
  n = len(first)
  m = len(second)
  lcs_table = [[0 for _ in range(n+1)] for _ in range(m+1)]
  for i in range(m):
    for v in range(n):
      if first[v] == second[i]:
        lcs_table[i+1][v+1] = lcs_table[i][v] + 1
      else:
        lcs_table[i+1][v+1] = max(lcs_table[i+1][v], lcs_table[i][v+1])

  return lcs_table[m][n]

print(lcs(first, second))