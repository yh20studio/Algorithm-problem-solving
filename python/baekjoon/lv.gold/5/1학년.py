# link : https://www.acmicpc.net/problem/5557
# Lv : gold 5
# Category : 다이나믹프로그래밍

# 덧셈과 뺄셈, 2가지 경우의 수를 무한하게 늘려나가는 큐를 이용한 계산을 하게되면, 2의 제곱형태로 나타나 시간초과가 난다.
# 따라서 나오는 계산 값들중 숫자가 같다면 한번에 처리할 수 있는 방법이 있을 것이고, 그게 다이나믹프로그래밍이다.
# 각 스텝마다 나오는 모든 계산값들을의 개수를 체크하고, 다음 단계에서는 모든 계산값들의 개수만큼 연산하는 것이 아닌, 
# 0~20까지의 숫자중 이전단계까지 계산 후 나오는 숫자들만 계산을 하고, 그 숫자의 counting 만 기록해주면 된다.

import sys 
# (3 ≤ N ≤ 100)
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0
# row: 주어지는 숫자들의 index, columns: 현재까지의 계산 값, 값 : 해당 row와 게산결과가 columns으로 나온 계산식의 개수
visited = [[0 for _ in range(21)]for _ in range(N)]

for i in range(N):
  if i == 0:
    visited[i][numbers[i]] = 1
  elif i == N-1:
    answer = visited[i-1][numbers[i]]

  else:
    for c in range(21):
      if visited[i-1][c] != 0:
        plus_result = c + numbers[i]
        if plus_result >= 0 and plus_result <= 20:
          visited[i][plus_result] += visited[i-1][c] 

        minus_result = c - numbers[i]
        if minus_result >= 0 and minus_result <= 20:
          visited[i][minus_result] += visited[i-1][c] 


print(answer)