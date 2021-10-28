# link : https://www.acmicpc.net/problem/1759
# Lv : gold 5
# Category : 조합, 구현

# 암호는 3글자 이상이다.
# 암호는 모음 1개, 자음 2개 이상을 꼭 포함해야한다.
# 가능한 암호는 알파벳 순서대로 구성되어야 한다.
# 가능한 암호를 알파벳 순서대로 나열한다.

from itertools import combinations

L, C = map(int, input().split())
li = list(map(str, input().split()))

comb = list(combinations(li, L))
sorted_combs = []

for tup in comb:
  sorted_combs.append(sorted(tup))

for string in sorted(sorted_combs):
  vowels = 0
  consonants =0
  for alphabet in string:
    if alphabet in 'aeiou':
      vowels += 1
    else:
      consonants += 1
  
  if vowels >= 1 and consonants >= 2:
    print("".join(string))