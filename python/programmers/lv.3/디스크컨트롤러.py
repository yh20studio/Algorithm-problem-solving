# link : https://programmers.co.kr/learn/courses/30/lessons/42627
# Lv : 3
# Category : 우선순위 큐

# 일이 처리되는 평균 시간의 최솟값을 구해야하는데, 이는 시작하는 일에 따라서 가장 적게 걸리는 일을 먼저 처리해야한다.
# 그래야 나머지 일들이 기다리는 시간이 적기 때문이다.
# 따라서 걸리는 시간을 기준으로 우선순위 큐를 만들고, 가능한 일이 많을때는 가장 적게 걸리는 일을 먼저처리하고, 
# 가능한 일이 없을 경우에는 다음 시간의 가장 빠른 일을 찾는다.


from heapq import heappush, heappop

def solution(jobs):
    answer = 0
    capabel_jobs = []
    queue_order_start = []
    jobs_start = [[] for _ in range(1001)]
    
    for i in range(len(jobs)):
        start, duration = jobs[i]
        jobs_start[start].append([duration, i])
        heappush(queue_order_start, [start, i])
    
    now = 0
    visited = []
    while len(visited) < len(jobs): 
        if now <= 1000: 
            for start in range(now+1):
                while jobs_start[start]:
                    duration, i = jobs_start[start].pop()
                    heappush(capabel_jobs, [duration, i]) 
        else:
            for start in range(1001):
                while jobs_start[start]:
                    duration, i = jobs_start[start].pop()
                    heappush(capabel_jobs, [duration, i]) 
        
        if len(capabel_jobs) > 0:
            duration, index = heappop(capabel_jobs)
            answer += (now + duration - jobs[index][0])
            now += duration    
            visited.append(index)
            
        else: # 만약 가능한 일이 없다면 다음 시간대에 가장 빠르게 시작하는 일을 가져온다.
            while True:
                start, index = heappop(queue_order_start)
                if index not in visited:
                    now = start
                    break
        
    return answer//len(jobs)