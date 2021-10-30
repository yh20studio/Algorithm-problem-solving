# link : https://programmers.co.kr/learn/courses/30/lessons/43105
# Lv : 3
# Category : 다이나믹프로그래밍

# 삼각형의 아래칸까지의 정수의 합을 계산할때 전 삼각형의 마지막 줄의 값이 쓰이기 때문에 다이나믹프로그래밍을 이용해서 풀었다.

def solution(triangle):
    answer = 0
    dp = []
    
    for r in range(len(triangle)):
        if r == 0:
            dp.append(triangle[r])
        else:
            for c in range(len(dp[r-1])):
                if c == 0:
                    triangle[r][c] += dp[r-1][c]
                else:
                    triangle[r][c] += max(dp[r-1][c-1], dp[r-1][c])
                
                if c == len(dp[r-1])-1:
                    triangle[r][c+1] += dp[r-1][c]    
            
            dp.append(triangle[r])
    answer = max(dp[len(triangle)-1])

    return answer