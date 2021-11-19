# link : https://programmers.co.kr/learn/courses/30/lessons/42586
# Lv : 2
# Category : 반복문

# 미리 선행되어 있는 일을 끝나야 그 다음 일을 같이 배포할 수 있습니다. 이때 날짜와 index 값을 점점 늘려가면서 비교를 해주었습니다.

def solution(progresses, speeds):
    answer = []
  
    days = 1
    index = 0
    count = 0
    while index < len(progresses): 
        if progresses[index] + speeds[index]*days >= 100:
            count += 1
            index += 1
            if index == len(progresses):
                answer.append(count)
        else:
            if count > 0 :
                answer.append(count)
                count = 0
            days += 1    
    
    return answer