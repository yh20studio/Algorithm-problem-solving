# link : https://programmers.co.kr/learn/courses/30/lessons/42578
# Lv : 2
# Category : 조합

# 모든 종류의 옷들 중에서, 각각을 종류별로 옷을 구분한다.
# 한 종류에서는 한번만 입을 수 있으므로 (해당 종류의 옷의 개수 +1(안입는 경우의 수))가 한 종류에서 나올 수 있는 가짓수이다.
# 따라서 이를 모두 곱해주고 모두다 안입는 경우의 수 1가지를 빼면 정답이다.

from itertools import combinations

def solution(clothes):
    answer = 0
    dic = {}
    category_list = []
    for name, category in clothes:
        if category in dic.keys():
            dic[category].append(name)
        else:
            dic[category] = [name]
            category_list.append(category)
        
    cnt = 1
    for category in category_list:
        cnt = cnt * (len(dic[category])+1)
    
    return cnt-1