# link : https://programmers.co.kr/learn/courses/30/lessons/12899
# Lv : 2
# Category : 이진법

# 이 문제는 이진법의 논리와 비슷한데 여기서는 1, 2, 4 이렇게 3개의 숫자를 활용하는 것입니다. 
# 따라서 일반적인 이진법을 하는 것처럼 주어진 숫자를 3의 제곱 형태로 최대한 분리해준다음 진행하면 쉽습니다.

def solution(n):
    answer = ''
    count = 0
    
    while n >= 3 ** count:
        n -= 3 ** count
        count+=1
    
    while count > 0:
        a = 0
        count -= 1
        while n >= 3 ** (count):
            n -= 3 ** (count)
            a+=1
        if a == 0:
            answer += '1'
        elif a == 1:
            answer += '2'
        elif a == 2:
            answer += '4'
    
    return answer