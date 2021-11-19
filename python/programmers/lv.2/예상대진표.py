# link : https://programmers.co.kr/learn/courses/30/lessons/12985
# Lv : 2
# Category : 나눗셈

# 주어진 대결 순서가 있는데, 대진은 1:1로 붙으며, 부전승이 없다고 가정할 때 2의 나누기를 통해서 
# 언제 해당하는 선수들이 붙을 지 계산할 수 있다.

def solution(n,a,b):
    answer = 1
    
    while True:
        
        if a // 2 != b // 2 and abs(a-b) == 1:
            break
        
        if a % 2 == 0:
            a = a//2
        else:
            a = (a+1)//2

        if b % 2 == 0:
            b = b//2
        else:
            b = (b+1)//2
            
        answer += 1
    
    return answer