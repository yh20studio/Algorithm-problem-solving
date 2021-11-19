# https://programmers.co.kr/learn/courses/30/lessons/86491
# Weekly Challenge
# Category : 구현

def solution(sizes):
    answer = 0
    wallet = [0, 0]
    for r, c in sizes:
        if r >= c:
            wallet[0] = max(wallet[0], r)
            wallet[1] = max(wallet[1], c)
        else:
            wallet[0] = max(wallet[0], c)
            wallet[1] = max(wallet[1], r)

    answer = wallet[0]*wallet[1]
    
    return answer