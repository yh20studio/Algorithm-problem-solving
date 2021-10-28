# link : https://www.acmicpc.net/problem/1149
# Lv : silver 1
# Category : 다이나믹프로그래밍

# 집을 색칠하는 비용에 대한 것을 점점 반복문을 지날수록 업데이트 되는 환경으로 코드를 짰다.
# 결국 이전에 했던 계산이 현재 계산에 영향을 미치기 때문에 dp알고리즘을 활용하여 문제를 풀지 않았나 싶다.

n = int(input())
rgb = []

for _ in range(n):
  rgb.append(list(map(int, input().split())))

for i in range(n):
  p = rgb[i]

  if i == n-1:
    nex = [0, 0, 0]
  else:
    nex = rgb[i+1]
  
  nex[0] = min(nex[0] + p[1], nex[0] + p[2]) 
  nex[1] = min(nex[1] + p[0], nex[1] + p[2])
  nex[2] = min(nex[2] + p[0], nex[2] + p[1]) 

print(min(rgb[n-1]))