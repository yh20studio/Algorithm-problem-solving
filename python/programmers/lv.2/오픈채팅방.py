# link : https://programmers.co.kr/learn/courses/30/lessons/42888
# Lv : 2, 2019 KAKAO BLIND RECRUITMENT
# Category : Dictionary, 구현

# 이 문제는 Log 값을 보고 Message를 출력하는 것입니다. 
# 그런데 유저의 nickName 값이 변할 수가 있으므로 각 유저의 고유 id 값을 통해서 Message를 저장하는 것이 중요합니다. 
# 따라서 배열을 만든 다음 각 Message의 순서를 저장한 후 마지막에 닉네임이 바뀐 것을 적용한 Message를 출력해주면 됩니다.

def solution(record):
    answer = []
    messageList = []
    userList = {}
    for log in record:
        logList = log.split(" ")
        actionLog = ""
        if logList[0] == 'Enter':
            actionLog = "들어왔습니다."
            userList[logList[1]] = logList[2]
            messageList.append([logList[1], actionLog])
        elif logList[0] == 'Leave':
            actionLog = "나갔습니다."
            messageList.append([logList[1], actionLog])
        elif logList[0] == 'Change':
            userList[logList[1]] = logList[2]
            
        
        
    for userId, actionLog in messageList:
        nickName = userList[userId]
        answer.append(f"{nickName}님이 {actionLog}")
    
    return answer