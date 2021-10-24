# link : https://programmers.co.kr/learn/courses/30/lessons/17676
# Lv : 3, 2018 KAKAO BLIND RECRUITMENT
# Category : 파싱, 부동소수점

# 시작 시간과 끝나는 지점을 기준으로만 최대 처리량을 계산하기로 했다.
# 주어진 log 데이터를 int형으로 변환한다.
# (시작 시간, 끝나는 시간) 배열을 한개 만들어 주고, 각 시간의 구분 없이 추가한 배열도 만든다.
# 두 배열을 모두 시간에 대한 오름차순으로 정리해준다.
# 반복문을 통해서 각 시간에 대한 최대 처리량을 계산해준다. 
# 여기서 반복적인 계산이 나타날 수 있으므로 만약 해당하는 값이 아니라면 반복을 종료하는 코드로 같이 작성한다.

def solution(lines):
    answer = 0
    logData = []
    timeList = []

    for index in range(len(lines)):
        
        days, time, duration = lines[index].split(" ")
        hour, minute, second = time.split(":")
        endTime = int((int(hour)*3600 + int(minute)*60 + float(second))*1000)
        durationList = list(duration)
        durationList.pop()
        durationTime = float("".join(durationList))
        
        startTime = endTime - int(durationTime*1000) + 1
        
        logData.append((startTime, endTime))
 
        if startTime == endTime:
            timeList.append(startTime)
        else:
            timeList.append(startTime)
            timeList.append(endTime)
        
    logData = sorted(logData)
    timeList = sorted(timeList)
 
    
    for i in range(len(timeList)):
    
        time = timeList[i]
        addOneSecond = time + 999
        count = 0
        for v in range(len(logData)):
            start_time, end_time = logData[v]
            
            if addOneSecond >= start_time and time <= end_time:
                count += 1
            else:
                if addOneSecond < start_time:
                    break
        answer = max(answer, count)
        
    return answer