# link : https://www.acmicpc.net/problem/1011
# Lv : gold 5
# Category : 구현, 수학적 사고

# 출발할때 1, 도착할때 1의 속도로 와야하므로 121, 12321, 12221, 등 앞 뒤가 비슷한 모양으로 숫자가 배열된다고 생각했다.
# 따라서 단계적으로 k 값을 늘려가면서 진행을 하지만, 최종 거리에서 k값의 2배를 빼는 작업을 하면서 계산을 진행했다.

import sys  
answer = []
# 테스트 케이스 갯수
T = int(sys.stdin.readline())

for _  in range(T):
  start, end = map(int, sys.stdin.readline().split())
  d = end - start
  cnt = 0 
  k = 0
  while d > 0:
    k+= 1
    d -= 2*k
    # 만약 d = 1 일 경우에는 정답이 1이므로 예외처리를 했다.
    if k == 1 and d <= 0:
      answer.append(1)
      break
    # 남은 거리 값이 0 보다 작다면 총 숫자 배열의 개수가 짝수개가 되는 경우이므로 k*2이 정답이 된다.
    if d<= 0:
      answer.append(k*2)
      break
    # 남은 거리 값이 0보다는 크고 k+1값보다 작다면 총 숫자 배열의 개수가 홀수개가 되는 경우가 나오기 때문에 총 횟수는 k*2 + 1이 된다.
    elif d <= k+1:
      answer.append(k*2 + 1)
      break

for number in answer:
  print(number)
