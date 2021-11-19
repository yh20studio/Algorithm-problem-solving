# link : https://www.acmicpc.net/problem/7662
# Lv : gold 5
# Category : 우선순위 큐

# 우선순위 큐를 최댓값, 최솟값을 통해서 2개를 만든다. 그리고 삭제 요청이 왔을 때 해당 데이터와 맞는 곳에서 삭제시켜주면 되는데
# 우선순위 큐를 2개를 만들면서 생기는 중복 값을 처리하기 어려워진다. 따라서 dictionary를 이용해서 insert 된 값들을 추적하면서
# 삭제, 삽입을 하게된다면 문제가 해결된다.

import sys
from heapq import heappop, heappush

TC = int(sys.stdin.readline())

for _ in range(TC):
  asc_queue = []
  desc_queue = []
  remain_count = 0
  dic = {}
  # k (k ≤ 1,000,000)
  k = int(sys.stdin.readline())
  for _ in range(k):
    mode, number = map(str, sys.stdin.readline().split())
    if mode == "I":
      if int(number) in dic.keys():
        dic[int(number)] += 1
      else:
        dic[int(number)] = 1
      remain_count+= 1
      heappush(asc_queue, int(number))
      heappush(desc_queue, -int(number))
    elif mode == "D":
      if int(number) == 1 and len(desc_queue) > 0:
        remain_count-=1
        remove = -heappop(desc_queue)
        while dic[remove] == 0:
          remove = -heappop(desc_queue)

        dic[remove] -= 1
        
      elif int(number) == -1 and len(asc_queue) > 0:
        remain_count-=1
        remove = heappop(asc_queue)
        while dic[remove] == 0:
          remove = heappop(asc_queue)

        dic[remove] -= 1
      
      if remain_count == 0:
        asc_queue = []
        desc_queue = []
  
  if remain_count > 0:
    min_number = heappop(asc_queue)
    while dic[min_number] == 0:
      min_number = heappop(asc_queue)
    
    max_number = -heappop(desc_queue)
    while dic[max_number] == 0:
      max_number = -heappop(desc_queue)

    if min_number > max_number:
      print("EMPTY")
    else:
      print(f"{max_number} {min_number}")  

  else:
    print("EMPTY")