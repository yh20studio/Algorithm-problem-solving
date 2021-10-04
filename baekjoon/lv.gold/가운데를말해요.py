# link : https://www.acmicpc.net/problem/2042
# Lv : gold
# Category : 우선순위 큐, 구현

# 여러가지의 방법이 있으나 시간초과 현상으로 왼쪽, 오른쪽 우선순위큐를 2개를 사용해서 각각 구현하여 비교하는 것이 빠르다.

import sys  
from heapq import heappush, heappop

N = int(sys.stdin.readline())

left_heapq = []
right_heapq = []
left_max = 0
right_min = 0

for i  in range(N):
  number = int(sys.stdin.readline())
  if i ==0:
    heappush(left_heapq, -number)
    left_max = number
    print(number)
  else:
    # left_max 와 right_min 값을 pop 없이 지정하기 위함.
    left_max = -left_heapq[0]
    if len(right_heapq) != 0:
      right_min = right_heapq[0]

    # 오른쪽 우선 순위 큐가 개수가 많을 경우
    if len(left_heapq) < len(right_heapq):
      if number <= right_min:
        heappush(left_heapq, -number)
        
        if left_max < number:
          print(number)
        
        else:
          print(left_max)

      else:
        heappop(right_heapq)
        heappush(left_heapq, -right_min)
        print(right_min)
        heappush(right_heapq, number)

    # 우선 순위 큐가 개수가 같을 경우
    elif len(left_heapq) == len(right_heapq):
      if number <= left_max:
        print(left_max)
        heappush(left_heapq, -number)

      else:
        if right_min < number:
          print(right_min)

        else:
          print(number)  

        heappush(right_heapq, number)

    # 왼쪽 우선 순위 큐가 개수가 많을 경우
    else:
      if number < left_max:
        heappush(right_heapq, left_max)
        left_max = -heappop(left_heapq)

        if len(left_heapq) != 0 :
          left_max2 = -left_heapq[0]
          heappush(left_heapq, -number) 

          if left_max2 < number:
            print(number)

          else:
            print(left_max2)

        else:
          heappush(left_heapq, -number) 
          print(number)
         
      else:
        print(left_max)
        heappush(right_heapq, number)
        