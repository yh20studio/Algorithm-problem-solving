# link : https://programmers.co.kr/learn/courses/30/lessons/77485
# Lv : 2
# Category : 구현

# 행렬이 rotate할 때 가장자리만 도는 경로가 있으므로 이 경로를 잘 따라갈 수 있도록 조건문들 통해서 구현하는 문제이다. 

def solution(rows, columns, queries):
    answer = []
    
    # 행렬에는 1부터 rows x columns까지의 숫자가 한 줄씩 순서대로 적혀있습니다. 
    matrix = [[c + (r-1)*(columns) for c in range(columns+1) ] for r in range(rows+1)]
    
    
    for x1, y1, x2, y2 in queries:
        min_visited = rows * columns
        change_number =  matrix[x1][y1]
        r, c = [x1, y1]
        first = True
        while True:
            if first:
                first = False
            else:
                if [r, c] == [x1, y1]:
                    break
                
            if r == x1: # 오른쪽 방향 전진
                if c == y2:
                    r += 1
                else:
                    c += 1
            elif r == x2: # 왼쪽 방향 전진
                if c == y1:
                    r -= 1
                else:
                    c -= 1
            
            else: 
                if c == y1: # 위쪽 방향 전진
                    r -= 1
                    if r == x1:
                        last = True
                        
                else: # 아래쪽 방향 전진
                    r += 1
            
            # 숫자 변경
            occupy_number = matrix[r][c]
            matrix[r][c] = change_number
            min_visited = min(min_visited, change_number)
            change_number = occupy_number
        
        answer.append(min_visited)

    return answer