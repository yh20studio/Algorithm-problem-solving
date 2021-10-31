# link : https://www.acmicpc.net/problem/1717
# Lv : gold 4
# Category : 유니온파인드

# 합잡합과, 집합에 포함되어있는지를 확인하는 문제이므로, 
# 각각의 집합을 합치는 과정을 유니온 함수
# 루트노드를 찾아나가는 과정을 파인드 함수로 정의해서 사용한다.
# 비효율적인 find를 없애기 위해서 union 과정에서 노드의 정보가 루트가 아닌 경우에는 찾아서 딕셔너리를 다시 업데이트 해주는 방식을 사용

import sys

def find_parent(x):  
  if info[x] != x:
    return find_parent(info[x])
  return info[x]

def union(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a == b:
    return
  elif a < b:
    info[b] = a
  elif a > b:
    info[a] = b

def solve():
  for index in range(m):
    kinds, a, b = map(int, sys.stdin.readline().split())
    if kinds == 0:
      union(a, b)
    elif kinds == 1:
      if find_parent(a) == find_parent(b):
        print("YES")
      else:
        print("NO")

sys.setrecursionlimit(10**5)
n, m = map(int, sys.stdin.readline().split())
info = [i for i in range(n+1)]
solve()