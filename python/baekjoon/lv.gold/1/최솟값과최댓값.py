# link : https://www.acmicpc.net/problem/2357
# Lv : gold 1
# Category : 세그먼트 트리

# 주어진 순서쌍을 이용해서 해당 범위내에서 최대, 최솟값을 찾아야 함.
# 순서쌍이 주어질 때마다 최대, 최솟값을 계산한다면 시간이 오래걸릴 것이므로, 계산한 값을 저장해서 사용하는 DP를 이용하려고 했으나,
# N의 값이 커서 메모리 초과현상이 일어났다. 따라서 세그먼트 트리를 사용하기로 함.

import sys  

def init(start, end, index):
  if tree[index] != [0, 0]:
    return tree[index]
  
  if start == end:
    tree[index] = [numbers[start], numbers[start]]
    return tree[index]
  
  mid = (start + end)//2
  a, b = init(start, mid, index*2)
  c, d = init(mid+1, end, index*2 + 1)
  if a > c:
    a = c
  if b < d:
    b = d
  tree[index] = [a, b]

  return tree[index]

def query(start, end, index, qLeft, qRight):
  
  if start > qRight or end < qLeft:
    return [1000000001, 0]

  if start >= qLeft and end <= qRight:
    return tree[index]
    
  mid = (start + end)//2

  a, b = query(start, mid, index*2, qLeft, qRight)
  c, d = query(mid+1, end, index*2+1, qLeft, qRight)

  return [min(a, c), max(b, d)]

    
answer = []
N, M = map(int, (sys.stdin.readline().split()))
# 순서쌍에서 사용되는 index는 1부터 시작하므로 numbers에도 데이터를 1 부터 받기 위함.
numbers = [0]
orders = []  

for _ in range(N):
  numbers.append(int(sys.stdin.readline()))

for _ in range(M):
  orders.append(list(map(int, (sys.stdin.readline().split()))))

tree =[[0, 0] for _ in range((N*4))]
init(1, N, 1)

for a, b in orders:
  minimum, maximum = query(1, N, 1, a, b)
  print(f"{minimum} {maximum}")


