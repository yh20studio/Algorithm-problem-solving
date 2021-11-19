# link : https://programmers.co.kr/learn/courses/30/lessons/12973
# Lv : 2
# Category : 스택

# 스택을 이용해서 이전 문자를 관리해주면서 짝을 지어 제거해줍니다. 

def solution(s):
    answer = -1
    stringList = list(s)
    stack = []
    
    for i in range(len(stringList)):
        if len(stack) == 0: # 바로 전 문자가 없다면 짝을 지을 수 없기 때문에 검증과정을 안거친다.
            stack.append(stringList[i])
        
        else:
            prev_char = stack.pop() # 바로 전 문자
            if prev_char != stringList[i]:
                stack.append(prev_char)
                stack.append(stringList[i])
            
    
    # 성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.
    if len(stack) == 0:
        return 1
    else:
        return 0