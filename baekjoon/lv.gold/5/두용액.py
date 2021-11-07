# link : https://www.acmicpc.net/problem/2470
# Lv : gold 5
# Category : 이분탐색

# 이 문제는 전체 용액의 갯수가 매우 크므로 일반적인 반복문으로 시간내에 통과할 수가 없었다.
# 따라서 주어진 용액을 기준으로 해서 해당 용액과 섞이면 최대한 0에 가까운 용액을 이분탐색을 통해서 찾는다.
# 이때 반복문이 끝나고 0이 되는 용액을 찾지 못했을 때 
# 찾아진 mid 값을 기준으로 mid-1, mid, mid+1 값 중 어느 것이 최대한 0에 가까운 값을 만드는지 모르기 때문에
# 이를 모두 비교 후 답을 찾아준다.

import sys 

# 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다. 
N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort() # 오름차순 정렬
mix_liquids = 2000000001
answer = []

for i in range(N):
  start = 0
  end = N-1
  target = -liquids[i]
  
  while start <= end : # 이분탐색
    mid = (start + end)//2
    if liquids[mid] < target:
      start = mid +1
    elif liquids[mid] > target:
      end = mid -1
    else:
      answer = [-target, liquids[mid]]
      break
      
  compare = []
  if mid == N-1:
    compare.append(mid)
    compare.append(mid-1)
  elif mid == 0:
    compare.append(mid)
    compare.append(mid+1)
  else:
    compare.append(mid-1)
    compare.append(mid)
    compare.append(mid+1)
  
  for index in compare:
    if index != i: # 본인과 섞이면 안된다.
      if mix_liquids > abs(liquids[i] + liquids[index]):
        answer = [liquids[i], liquids[index]]
        mix_liquids = abs(liquids[i] + liquids[index])

if answer[0] < answer[1]:
  print(f"{answer[0]} {answer[1]}") 
else:
  print(f"{answer[1]} {answer[0]}") 