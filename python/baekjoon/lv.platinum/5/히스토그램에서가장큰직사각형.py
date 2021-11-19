# link : https://www.acmicpc.net/problem/6549
# Lv : platinum 5
# Category : 세그먼트 트리, 분할정복

# 해당 문제는 히스토그램의 넓이를 구할 때 사용해야할 높이 값이 양 옆의 히스토그램의 영향을 받으므로, 
# 세그먼트 트리를 활용해서 히스토그램의 구간 별 최소 높이를 가지는 index를 저장해야한다. 
# 이를 활용해서 모든 구간에서 넓이를 구한 다음 최대값을 찾아야 하는 문제이다.
# 이때 모든 구간을 전부 탐색하게 된다면 n의 값이 크므로 시간초과가 발생한다.
# 따라서 세그먼트 트리에 저장되어 있는 구간별 최소 높이 인덱스를 중간으로 하여 히스토그램을 분할하여 넓이를 계산한다.

import sys  
sys.setrecursionlimit(100000)

# 트리 생성 및 초기화
def init(start, end, index):
  if trees[index] != 0:
    return trees[index]

  if start == end:
    trees[index] = start
    return trees[index]

  mid = (start + end)//2
  a = init(start, mid, index*2)
  c = init(mid+1, end, index*2+1)
  if histogram[a] > histogram[c]:
    trees[index] = c
  else:
    trees[index] = a
  return trees[index]

# 트리에서 구간별 최소 높이의 인덱스 찾기
def query(start, end, index, qLeft, qRight):
  if start > qRight or end < qLeft:
    return 0
  
  if qLeft <= start and end <= qRight:
    return trees[index]
  mid = (start + end)//2

  a = query(start, mid, index*2, qLeft, qRight)
  c = query(mid+1, end, index*2+1, qLeft, qRight)

  if a != 0 and c!= 0:
    if histogram[a] > histogram[c]:
      return c
    else:
      return a
  else:
    if a== 0:
      return c
    elif c == 0:
      return a
    
# 분할정복으로 넓이의 최댓값 찾기
def findLargest(start, end):
  if start > end:
    return 0
  if start == end:
    return histogram[start]
  minimumIndex = query(1, n, 1, start, end)
  
  a = query(1, n, 1, start, minimumIndex-1)
  c = query(1, n, 1, minimumIndex+1, end)

  return max(histogram[minimumIndex]*(end-start+1), 
  histogram[c]*(end-minimumIndex), 
  histogram[a]*(minimumIndex-start), 
  findLargest(minimumIndex+1, end), findLargest(start, minimumIndex-1))

# 문제 input
while True:
  histogram = list(map(int, (sys.stdin.readline().split())))
  if histogram[0] == 0:
    break
  n = histogram[0]
  trees = [0 for _ in range(n*4)]
  init(1, n, 1)
  answer = findLargest(1, n)
  print(answer)



