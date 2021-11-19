# link : https://programmers.co.kr/learn/courses/30/lessons/17677
# Lv : 2
# Category : 구현, 문자열

# 주어진 조건을 빠지지 않고 모두 조건문을 통해서 구현하면 된다.
# 이때 대문자, 소문자 차이를 구분하고, 알파벳이냐 아니냐를 구분할줄 알아야 한다.


import math

def toMultipleSet(st):
    dic = {}
    li_str = list(st)
    
    for i in range(len(li_str)-1):
        char = li_str[i]
        next_char = li_str[i+1]
        
        # 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다.
        if char.isalpha() == False:
            continue
        if next_char.isalpha() == False:
            continue
        # 대문자와 소문자의 차이는 무시한다.
        if char.isupper(): 
            char = char.lower()
        if next_char.isupper():
            next_char = next_char.lower()
            
        word = char + next_char
        
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    
    return dic

def solution(str1, str2):
    answer = 0
    
    # 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 
    dic_str1 = toMultipleSet(str1)
    dic_str2 = toMultipleSet(str2)
    intersection = 0
    union = 0
    
    for key, value in dic_str1.items():
        if key in dic_str2.keys():
            intersection += min(value, dic_str2[key])
            union += max(value, dic_str2[key])
        else:
            union += value
    
    for key, value in dic_str2.items():
        if key not in dic_str1.keys():
            union += value
    
    # 자카드 유사도 J(A, B)는 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값으로 정의된다.
    # 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
    if intersection == 0 and union == 0:
        answer = 1
    else:
        answer = intersection/union
    
    # 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.
    return math.trunc(answer * 65536)