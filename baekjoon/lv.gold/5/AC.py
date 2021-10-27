# link : https://www.acmicpc.net/problem/5430
# Lv : gold 5
# Category : 큐, 구현

# 입력으로 주어지는 것이 리스트 구조가 아닌, 리스트 구조를 문자열로 만든것으로 이 부분을 처리하기가 까다로웠다.
# 마찬가지로 출력이 리스트 형식이 아닌 문자열 형식으로 출력해야만 한다.
# 예를 들어 [1, 2] , [1,2] 이 두개는 출력이 다르다고 처리하기 때문에 이부분을 다시 파싱해서 리턴하는 부분이 까다로웠다.


import sys  
from collections import deque

answer = []
#  테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
T = int(sys.stdin.readline())

for i in range(T):
  error = False
  reverse = False
  # 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
  p = list(str(sys.stdin.readline()))[:-1]
  # 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
  n = int(sys.stdin.readline())
  # [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)
  li = list(sys.stdin.readline().rstrip().split(","))
  number_list = deque()
  
  for k in range(n): 
    number = li[k]
    if k == 0:
      number = number[1:]
    if k == n-1:
      number = number[:-1]
    
    number_list.append(int(number))

  for func in p:
    if func == 'R':
      if reverse:
        reverse = False
      else: 
        reverse = True

    elif func == 'D':
        if len(number_list) > 0:
          if reverse:
            number_list.pop()
          else:
            number_list.popleft()
        else:
          error = True
    
  if error:
    answer.append("error")
  else:
    queueToString = "["
    if reverse:
      while number_list:
        queueToString += str(number_list.pop())
        if len(number_list) != 0:
          queueToString += ","
    
      queueToString += "]" 
    else:
      while number_list:
        queueToString += str(number_list.popleft())
        if len(number_list) != 0:
          queueToString += ","
      
    
      queueToString += "]" 

    answer.append(queueToString)


for string in answer:
  print(string)

