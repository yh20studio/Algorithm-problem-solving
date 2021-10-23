# https://www.acmicpc.net/problem/7453
# Lv : gold
# Category : Dictionary

# 시간의 제한을 지키는 것이 매우 힘들었다.
# 이분탐색을 이용하여 찾아보는 것을 하려고 했지만 해당 방법보다 A+B 혹은 C+D에서 겹치는 부분을 좀더 쉽게 처리하도록 
# 파이썬의 Dictionary를 사용했다.

import sys  
from collections import defaultdict

# 배열의 크기 (1 ≤ n ≤ 4000)
N = int(sys.stdin.readline())
answer = 0
A_numbers = []
B_numbers = []
C_numbers = []
D_numbers = []

for i in range(N):
    a, b, c, d = map(int, (sys.stdin.readline().split()))
    A_numbers.append(a)
    B_numbers.append(b)
    C_numbers.append(c)
    D_numbers.append(d)

A_Plus_B = defaultdict(int)
for a in A_numbers:
    for b in B_numbers:
        A_Plus_B[a+b] += 1

for c in C_numbers:
    for d in D_numbers:
        if -(c+d) in A_Plus_B.keys():
            answer += A_Plus_B[-(c+d)]

print(answer)

