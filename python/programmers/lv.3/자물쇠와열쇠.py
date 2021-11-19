# link : https://programmers.co.kr/learn/courses/30/lessons/60059
# Lv : 3, 2020 KAKAO BLIND RECRUITMENT
# Category : 구현

# 키를 회전하고 이동시켜서 자물쇠를 열어야하는 문제이다.
# 키는 자유롭게 회전 및 이동이 가능하기 때문에 각 회전당, 각 x,y축 이동간 모든 경우의 수를 살펴보아야 한다.
# 함수를 구현하여 반복되는 계산과정을 보기 쉽게 표현했다.

def rotate(M, key): # 오른쪽 90도 회전
    new_key = []
    for i in range(M): 
        li = []
        for j in range(M):
            li.append(key[M-1-j][i])
        new_key.append(li)
        
    return new_key

def findJut(find_key, M): # 돌기 찾기
    jut = []
    for i in range(M):
        for j in range(M):
            if find_key[i][j]==1:
                jut.append([i,j])
    
    return jut

def findWhole(lock, N): # 홈 찾기
    whole = []
    for i in range(N):
        for j in range(N):
            if lock[i][j]==0:
                whole.append([i,j])
    
    return whole

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    whole = findWhole(lock, N)
    whole_cnt = len(whole)
    
    for i in range(4): # key값 총 회전을 3번하여 답을 찾아본다.
        jut = findJut(key, M)
        for x in range(-(M-1), N): # key를 x축으로 이동
            for y in range(-(M-1), N): # key를 y축으로 이동
                cnt = whole_cnt
                for r, c in jut:
                    new_r = r + y
                    new_c = c + x
                    
                    if new_r >=0 and new_r < N and new_c >= 0 and new_c < N:
                        if lock[new_r][new_c] == 0:
                            cnt -= 1
                        else:
                            break
        
                if cnt == 0: # lock의 모든 홈을 채웠을 때
                    answer = True
            
        key = rotate(M, key) # key 회전
    return answer
