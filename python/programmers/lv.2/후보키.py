# link : https://programmers.co.kr/learn/courses/30/lessons/42890
# Lv : 2, 2019 KAKAO BLIND RECRUITMENT
# Category : 조합, 구현

# 가능한 columns의 조합을 모두다 구해서 해당 값들로 유일성을 확인해야한다.
# 이때 모든 값을 다 구한다면 최소성을 만족할 수 없기 때문에 visited를 통해서 이미 구성이 완료된 조합을 통해서 최소성을 만족시켜야 한다.
# 조합의 반복문을 돌 때 이미 answer에 포함 시킨 columns 조합과 겹치는 경우는 반복문을 실행하면 안된다. 이는 최소성을 어기는 경우이기 때문이다.

from itertools import combinations

def solution(relation):
    answer = 0
    rows = len(relation)
    columns = len(relation[0])
    remain_columns = [i for i in range(columns)]
    comb = 1
    visited = []
    while comb <= columns:
        for comb_list in combinations(remain_columns, comb):
            minimality = True
            for visited_columns in visited:
                check = True
                for c in visited_columns:
                    if comb_list.count(c) == 0:
                        check = False
                if check:
                    minimality = False
                    break
            
            if minimality:
                dic = {}
                uniqueness = True
                for r in range(rows):
                    li = []
                    for c in comb_list:
                        li.append(relation[r][c])
                    st = ",".join(li)

                    if st in dic.keys():
                        dic[st]+= 1
                        uniqueness = False
                    else:
                        dic[st] = 1

                if uniqueness:
                    c_list = []
                    for c in comb_list:
                        c_list.append(c)
                    visited.append(c_list)
                    answer += 1

        comb += 1
    
    return answer