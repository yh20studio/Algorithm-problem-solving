# link : https://programmers.co.kr/learn/courses/30/lessons/60057
# Lv : 2, 2020 KAKAO BLIND RECRUITMENT
# Category : 문자열, BFS

# 문자열을 잘 파싱한뒤, 비교해주면 됩니다. 
# 이때 저는 deque를 사용하여서 남은 문자열과 이미 검사한 문자열로 나눠서 비교하는 방식을 선택했습니다. 
# 이러한 방식으로 겹치는 부분을 모두 카운트 한다음 조건에 맞게 출력해주면 됩니다.

from collections import deque

def solution(s):
    answer = 1001
    length = len(s)
    stringList = list(s)
   
    for i in range(1, length//2 + 2):
       
        stringDeque = deque(stringList)
        prevDeque = deque()
        
        while stringDeque:
            string = ""
            for v in range(i):
                if len(stringDeque) == 0:
                    break
                string += stringDeque.popleft()
                
            if len(prevDeque) == 0:
                prevDeque.append([1, string])
            else:
                count, prevString = prevDeque.pop()
                if prevString == string:
                    prevDeque.append([count+1, string])
                else:
                    prevDeque.append([count, prevString])
                    prevDeque.append([1, string])
        
        result = ""
        
        while prevDeque:
            count, string = prevDeque.popleft()
            if count == 1:
                result += f"{string}"
            else:
                result += f"{count}{string}"
    
        answer = min(answer, len(result))
        
    return answer