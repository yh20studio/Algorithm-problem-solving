# https://www.acmicpc.net/problem/2623
# Lv : gold 2
# Category : BFS

# 가수들끼리의 순서가 존재하는 것이며, 선행되어야 하는 순서가 존재하는 문제이다.
# 한 가수가 어떤 다른 가수들이 선행되어야 하는지 관리해야하며, 해당 가수가 대기열로 들어가면 다음은 누가 올 수 있는지 체크해야한다.
# 따라서 리스트와 딕셔너리를 활용하여 해당 과정을 체크해주었고, BFS를 통해서 순서를 탐색할 수 있도록 해주었다.

import sys  
from collections import deque

# 가수의 수 N과 보조 PD의 수 M
N, M = map(int, (sys.stdin.readline().split()))
singer_order = [[] for _ in range(N+1)]
before_singer = dict()

# 둘째 줄부터 각 보조 PD가 정한 순서들이 한 줄에 하나씩 나온다. 
for _ in range(M):
    # 각 줄의 맨 앞에는 보조 PD가 담당한 가수의 수가 나오고, 그 뒤로는 그 가수들의 순서가 나온다. 
    singer_list = list(map(int, (sys.stdin.readline().split())))
    singer_length = singer_list[0]

    # 가수들의 선후 관계를 표시한다.
    for i in range(1, singer_length):
        prev_singer = singer_list[i]
        next_singer = singer_list[i+1]
        singer_order[prev_singer].append(next_singer)
        if next_singer in before_singer.keys():
            before_singer[next_singer].append(prev_singer)
        else:
            before_singer[next_singer] = [prev_singer]

queue = deque()
visited = []
is_wait = [True for _ in range(N+1)]
# 자신 앞에 순서와 상관없이 맨 처음에 공연할 수 있는 가수 찾기
for i in range(1, N+1):
    if i not in before_singer.keys():
        queue.append(i)

while queue:
    singer = queue.popleft()
    if is_wait[singer]:
        is_wait[singer] = False
        for next in singer_order[singer]:
            # 가수가 준비가 되어있는가?
            is_ready = True
            for before in before_singer[next]:
                # 본인 순서보다 먼저 공연해야하는 가수들이 준비중인가?, 혹은 이미 대기열에 들어가 있는지를 판별
                if is_wait[before] == True:
                    is_ready = False
                    break
                
            if is_ready:
                queue.append(next)
        
        visited.append(singer)

# 만약 visited에 있는 가수가 전체 가수 숫자와 맞으면 출력하지만, 같지 않다면 불가능하다는 것이다.
if len(visited) == N:
    for singer in visited:
        print(singer)
else:
    print(0)
