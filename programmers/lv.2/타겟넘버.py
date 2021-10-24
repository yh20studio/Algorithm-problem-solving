# link : https://programmers.co.kr/learn/courses/30/lessons/43165
# Lv : 2
# Category : DFS

# 리스트를 사용해서 각각 차례대로 numbers에서 주어진 숫자를 빼고 더해주며 리스트를 최신화 했습니다. 
# 그리고 난 후 모든 과정이 끝났을 때 리스트의 들어있는 숫자들을 target과 비교하여 answer를 구했습니다.

def solution(numbers, target):
    answer = 0
    prev_list = [-numbers[0], numbers[0]]
    
    for i in range(1, len(numbers)):
        next_list = []
        for v in prev_list:
            num = v
            next_list.append(num-numbers[i])
            next_list.append(num+numbers[i])
            
        prev_list = next_list
    
    for k in prev_list:
        if k == target:
            answer += 1
            
    return answer