# link : https://programmers.co.kr/learn/courses/30/lessons/60058
# Lv : 2, 2020 KAKAO BLIND RECRUITMENT
# Category : 구현, 문자열

# 주어진 여러 조건을 if문과 반복문을 통하여 구현하는 문제이다. 이때 재귀함수가 사용되므로 함수를 정의하여 사용하는 것이 편하다고 판단했다.
# 문자열을 가지고 슬라이싱해야하는 상황이 주어지지만 list()를 이용해서 슬라이싱 하면 편하다.

def is_Correct(st):
    left = 0 # "("
    right = 0 # ")"
    
    for i in range(len(list(st))):
        char = list(st)[i]
                   
        if char == "(":
            left += 1
        else:
            right += 1
            if left == right:
                left = 0
                right =0
            elif left < right:
                return False

    if left == 0 and right ==0:
        return True
    else:
        return False

def split_u_v(st):
    left = 0 # "("
    right = 0 # ")"
    
    for i in range(len(list(st))):
        char = list(st)[i]
                   
        if char == "(":
            left += 1
        else:
            right += 1
        
        if left == right:
            return i

def toCorrect(st):
    if st == "": # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return ""
    
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 한다 -> 무조건 짝수 개
    index = split_u_v(st)
    u = st[0:index+1]
    v = st[index+1:]
        
    if is_Correct(u): # 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        return u + toCorrect(v)
    
    else:
        new_u = ""
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for i in range(len(u)):
            if i == 0 or i == len(u)- 1:
                continue
            else:
                if list(u)[i] == ")":
                    new_u += "("
                else:
                    new_u += ")"
    
        return "(" + toCorrect(v) + ")" + new_u
    

def solution(p):
    answer = ''
    
    if is_Correct(p): # 만약 p가 이미 "올바른 괄호 문자열"이라면 그대로 return 하면 됩니다.
        answer = p
    else:
        answer = toCorrect(p)

    return answer