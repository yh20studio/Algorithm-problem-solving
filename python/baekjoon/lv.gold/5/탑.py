# link : https://www.acmicpc.net/problem/2493
# Lv : gold 5
# Category : 스택

# 레이저를 맞아줄 수 있는 타워들을 차레대로 스택에 저장하면서 답을 구하면 된다.
# 이 문제가 시간초과로부터 까다로웠던 이유은 출력을 list의 문자열 형태로 내보냈어야 하기 때문이다.
# 매번 str += "index" 이렇게 더하게 되면 시간복잡도가 len(str) + len(index)로 되므로 상당히 오래걸린다.
# 따라서 리스트로 모든 answer을 구한다음 마지막에 *answer로 문자열 형태로 표현해주기로 한다.

import sys  

# N은 1 이상 500,000 이하이다.
N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = []

tower_height = {}
capable_tower = []

for i in range(N):
  if i == 0:
    answer.append(0)
    capable_tower.append(i)
  
  else:
    check = False
    while capable_tower:
      index = capable_tower.pop()
      if tower[i] <= tower[index]:
        answer.append(index+1)
        capable_tower.append(index)
        check = True
        break
    
    if check == False:
      answer.append(0)
    
    capable_tower.append(i)

print(*answer)
