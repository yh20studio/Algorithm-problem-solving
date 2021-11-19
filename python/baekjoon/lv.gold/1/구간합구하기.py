# link : https://www.acmicpc.net/problem/2042
# Lv : gold 1
# Category : 세그먼트 트리

import sys  

def init(start, end, index):
  if trees[index] != 0:
    return trees[index]

  if start == end:
    trees[index] = numbers[start]
    return trees[index]

  mid = (start + end)//2
  trees[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
  return trees[index]

def query(start, end, index, qLeft, qRight):
  if start > qRight or end < qLeft:
    return 0

  if start >= qLeft and end <= qRight:
    return trees[index]
  
  mid = (start + end)//2
  return query(start, mid, index*2, qLeft, qRight) + query(mid+1, end, index*2+1, qLeft, qRight)

def change(index, number, before):
  if index !=0 :
    trees[index] = trees[index] - before + number
    change(index//2, number, before)

def findIndex(start, end, target, index):
  if start == end and start == target:
    return index

  mid = (start + end)//2

  if start <= target and mid >= target:
    return findIndex(start, mid, target, index*2)

  if mid+1 <= target and end >= target:
    return findIndex(mid + 1, end, target, index*2 + 1)

N, M, K = map(int, (sys.stdin.readline().split()))
numbers = [0, ]
trees = [0 for _ in range(N*4)]
orders = []

for _ in range(N):
  numbers.append(int(sys.stdin.readline()))

for _ in range(M+K):
  orders.append(list(map(int, sys.stdin.readline().split())))

init(1, N, 1)
for a, b, c in orders:  
  if a == 1:
    tree_index = findIndex(1, N, b, 1)
    change(tree_index, c, trees[tree_index])
  else:
    print(query(1, N, 1, b, c))