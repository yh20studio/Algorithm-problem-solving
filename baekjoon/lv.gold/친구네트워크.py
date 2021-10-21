# link : https://www.acmicpc.net/problem/4195
# Lv : gold
# Category : 유니온 파인드

# 각 Name이 주어지고 연결 네트워크를 구성하는 문제이다.
# 해당 문제에서 root를 통해서 네트워크를 관리하고 만약, 주어진 이름의 root값이 달라서 서로 합쳐야하는 상황일때 Union함수를 통해서 합쳐준다.

import sys  

# 테스트 케이스 갯수
N = int(sys.stdin.readline())
answer = []

# root를 찾기 위한 함수
def find(target):
  if friend_relationship[target] == target:
    return target
  
  friend_relationship[target] = find(friend_relationship[target])
  return friend_relationship[target]
  
# 서로 다른 2개의 값이 주어졌을 때 각 root들을 합치는 함수
def union(a, b):
  root_a = find(a)
  root_b = find(b) 

  if root_a > root_b:
    friend_relationship[root_a] = root_b
    friend_cnt[root_b] += friend_cnt[root_a]
    return friend_cnt[root_b]
  
  elif root_a < root_b:
    friend_relationship[root_b] = root_a
    friend_cnt[root_a] += friend_cnt[root_b]
    return friend_cnt[root_a]
  
  # 만약 root가 같다면 서로 유니온 할 필요 없다.
  else:
    return friend_cnt[root_a]
  
      
for _ in range(N):
  F = int(sys.stdin.readline())
  friend_relationship = [0,]
  friend_cnt = [0,]
  users = {}
  person_count = 1
  for _ in range(F):
    person1, person2 = map(str, (sys.stdin.readline().split()))
    person1_index = 0
    person2_index = 0

    if person1 in users.keys():
      person1_index = users[person1]
    else:
      users[person1] = person_count
      person1_index = person_count
      friend_relationship.append(person_count)
      friend_cnt.append(1)
      person_count+=1
    
    if person2 in users.keys():
      person2_index = users[person2]
    else:
      users[person2] = person_count
      person2_index = person_count
      friend_relationship.append(person_count)
      friend_cnt.append(1)
      person_count+=1
    
    answer.append(union(person1_index, person2_index))

  
for number in answer:
  print(number)