# link : https://www.acmicpc.net/problem/14226
# Lv : gold 5
# Category : BFS

# 삭제, 붙여넣기, 복사하기를 상황에 맞게 쓰일 수 있도록 구현을 해준 상태로, BFS를 통한 가장 빠른 시간을 탐색하면 된다.
# 이때 같은 이모티콘 수, 같은 클립보드 수를 가진 곳을 다시 방문하여 중복됨을 방지하기 위해서 visited를 2차원 배열로 구현했다.

import sys
from collections import deque

# S (2 ≤ S ≤ 1000)
S = int(sys.stdin.readline())
answer = 0
visited = [[-1 for _ in range(1001)] for _ in range(1001)]
queue = deque()
queue.append([1, 0, 0])

while queue:
  emoji_cnt, clipboard, timer = queue.popleft()
  if emoji_cnt == S:
    answer = timer
    break
  if visited[emoji_cnt][clipboard] == -1:
    if emoji_cnt > 0: # 삭제
      queue.append([emoji_cnt-1, clipboard, timer+1])
      
      if emoji_cnt > clipboard: # 클립보드에 복사
        queue.append([emoji_cnt, emoji_cnt, timer+1])

    # 화면에 붙여넣기
    if clipboard != 0 and emoji_cnt+clipboard < 1001: 
      queue.append([emoji_cnt+clipboard, clipboard, timer+1])

    visited[emoji_cnt][clipboard] = 1

print(answer)