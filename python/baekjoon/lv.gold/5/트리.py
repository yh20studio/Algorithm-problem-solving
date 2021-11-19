# link : https://www.acmicpc.net/problem/1068
# Lv : gold 5
# Category : 트리, 큐

# 제거할 노드를 제거한 후 해당 노드를 root로 가지는 노드들 또한 연속적으로 지워준다.
# 모든 과정이 끝난 후 리프 노드를 찾아서 답을 낸다.

import sys 
from collections import deque

# 첫째 줄에 트리의 노드의 개수 N이 주어진다.
N = int(sys.stdin.readline())
node_root = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
answer = 0

queue = deque()
queue.append(remove_node)
remain_node = []

while queue: # 노드 삭제
  remove = queue.popleft()
  node_root[remove] = -2 # 노드가 삭제되었디.
  for node in range(len(node_root)):
    root = node_root[node]

    if root == remove:
      queue.append(node)

for i in range(len(node_root)): # 리프 노드 찾기
  if node_root[i] != -2:
    if i not in node_root:
      answer += 1
  

print(answer)

