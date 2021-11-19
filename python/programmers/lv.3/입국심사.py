# link : https://programmers.co.kr/learn/courses/30/lessons/43238
# Lv : 3
# Category : 이분탐색


def solution(n, times):
    answer = 0
    times.sort()
    start = 0
    end = times[0]*n
    sumPeople = 0
    
    while start <= end:
        sumPeople = 0
        mid = (start + end)//2 
        for time in times:
            sumPeople += mid//time

        if sumPeople >= n:
            answer = mid
            end = mid - 1
        elif sumPeople < n:
            start = mid + 1
    
  
    return answer