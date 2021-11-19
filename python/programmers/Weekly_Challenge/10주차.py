# https://programmers.co.kr/learn/courses/30/lessons/87377
# Weekly Challenge
# Category : 역행렬, 구현

# 좌표평면의 Range 구하기
def findMaxMin(x, y):
    global x_max, x_min, y_max, y_min
    
    x_max = max(x, x_max)
    x_min = min(x, x_min)
    y_max = max(y, y_max)
    y_min = min(y, y_min)

# 역행렬을 통해서 교점 구하기
def inverse_matrix(i, j, line, dots):
    x_1, y_1, c_1 = line[i]
    x_2, y_2, c_2 = line[j]
    
    # 교점이 있을 때만 함수 실행
    if x_1*y_2 - y_1*x_2 != 0:
        # ad - bc
        divisor = x_1*y_2 - y_1*x_2
        x_Q = (y_2*(-c_1) + y_1*c_2)
        y_Q = x_2*c_1 + x_1*(-c_2)

        # 교점의 좌표가 정수일 때만 함수 실행
        if x_Q%divisor ==0 and y_Q%divisor == 0:
            x = x_Q//divisor
            y = y_Q//divisor
            if y in dots.keys():
                dots[y].append(x)
            else: 
                dots[y] = [x]
            findMaxMin(x, y)
    
def solution(line):
    answer = []
    n = len(line)
    dots = {}
    ordered_dots = {}
    
    global x_max, x_min, y_max, y_min
    
    x_max = -float('inf')
    x_min = float('inf')
    y_max = -float('inf')
    y_min = float('inf')
 
    for i in range(n):    
        for j in range(i+1, n):
            inverse_matrix(i, j, line, dots)
    
    x_length = x_max - x_min +1
    y_length = y_max - y_min +1
    
    for y, value in dots.items():
        ordered_dots[-y+y_max] = value
        
    default_string_list = ['.' for _ in range(x_length)]
    default_string = ''.join(default_string_list)
    
    answer = [default_string for _ in range(y_length)]
    
    for row, value in ordered_dots.items():
        for x in value:
            answer[row] = f"{answer[row][:x-x_min]}*{answer[row][x-x_min+1:]}"
            
   
    return answer