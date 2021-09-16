# link : https://programmers.co.kr/learn/courses/30/lessons/86048
# Weekly Challenge
# Category : 구현

def solution(enter, leave):
    people = len(enter)
    answer = []
    people_state = [False for _ in range(people+1)]
    meet = {i : [] for i in range(1, people+1)}
    room = []
    enter_cnt = 0
    leave_cnt = 0
    
    while enter_cnt < people and leave_cnt < people:
        if people_state[leave[leave_cnt]] == True:
            room.remove(leave[leave_cnt])
            people_state[leave[leave_cnt]] = False
            leave_cnt += 1
        else:
            room.append(enter[enter_cnt])
            people_state[enter[enter_cnt]] = True
            enter_cnt += 1

            if len(room) >= 2:
                for number in room:
                    meet[number].extend(room)
    
    for person, li in meet.items():
        if len(li) == 0:
            answer.append(0)
        else:
            answer.append(len(set(li)) - 1)
    
    return answer