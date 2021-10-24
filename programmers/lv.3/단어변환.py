# link : https://programmers.co.kr/learn/courses/30/lessons/43165
# Lv : 3
# Category : DFS

# 해당 문제는 문자열을 비교하면서 깊이 탐색으로 해결했습니다. 
# 각 단어들을 List에 담아서 1가지 문자만 다른 경우에만 Stack에 넣는 방법을 선택했으며 DFS를 이용하여 탐색을 진행했습니다. 
# 또한 마지막에 만약 단어 변환이 불가능하다고 하면 0을 return 해야하는 조건을 만족시켜주기 위하여 코딩을 했습니다.

def solution(begin, target, words):
    answer = 0
    
    stack = [begin,]
    visited = []
    
    while stack:
        n = stack.pop()
        list_n = list(n)
        if n not in visited:
            visited.append(n)
            for st in words:
                count = 0
                list_st = list(st)
                for i in range(len(list_n)):
                    if list_n[i] == list_st[i]:
                        count += 1
                if count == (len(list_n) - 1):
                    stack.append(st)
    
    if target in visited:
        answer = visited.index(target)
    else:
        answer = 0

    return answer