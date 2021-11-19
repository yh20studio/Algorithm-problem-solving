# link : https://www.acmicpc.net/problem/1107
# Lv : gold 5
# Category : 브루트포스

# 리모콘을 이용하여 최대한 적은 버튼을 눌러서 원하는 채널에 도착하는 방법을 물어보는 문제이다.
# 처음에는 주어지는 채널에서 망가진 버튼의 유무를 판별하고, 가장 근처에 도달할 수 있는 채널을 찾아서
# 오름차순으로 도착하는 방법과 내림차순으로 도착하는 방법 중 최솟값을 도출하려고 했다.
# 하지만 각 자리수의 값에 따라서 어느 채널이 온전한 버튼으로 가장 가까운 채널인지 알아내기가 힘들었다.
# 따라서 주어진 채널과 비슷한 온전한 버튼으로 갈 수 있는 모든 채널을 찾고 최솟값을 도출하기로 했다.


import sys  
from collections import deque
#  N (0 ≤ N ≤ 500,000)
N = int(sys.stdin.readline())
# 고장난 버튼의 개수 M (0 ≤ M ≤ 10)
M = int(sys.stdin.readline())

if M != 0:
  broken_buttons = list(map(int, sys.stdin.readline().split()))
else:
  broken_buttons = []

capabel_buttons = [i for i in range(10)]
for button in broken_buttons:
  capabel_buttons.remove(button)

# 수빈이가 지금 보고 있는 채널은 100번이다.
channel = 100

answer = 500001
capabel_channel = deque([0])

for i in range(0, len(str(N))+1):
  length = len(capabel_channel)
  for _ in range(length):
    ch = capabel_channel.popleft()
    for number in capabel_buttons:
      new_ch = ch + number * (10 ** i)
      answer = min(answer, abs(N-new_ch) + i+1)
      capabel_channel.append(new_ch)
  
answer = min(answer, abs(N - 100))

print(answer)

