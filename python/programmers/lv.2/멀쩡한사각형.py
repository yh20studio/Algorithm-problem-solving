# link : https://programmers.co.kr/learn/courses/30/lessons/62048
# Lv : 2
# Category : 최대 공약수

# 수학적인 생각을 도와주는 문제입니다. 최대 공약수를 이용해서 문제를 풀면 쉽게 풀 수 있습니다!!

def solution(w,h):
    answer = w * h
    x, y = w, h
    
    while y:
        x, y = y, x % y
    
    minRect = (w // x) + (h // x) - 1
    answer -= x*minRect
    
    return answer