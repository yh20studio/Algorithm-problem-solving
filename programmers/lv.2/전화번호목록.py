# link : https://programmers.co.kr/learn/courses/30/lessons/42577
# Lv : 2
# Category : 접두사

# 알파벳순으로 정렬하여 서로 비교한다면, 한 전화번호와 전체를 비교할 필요가 없어진다. 
# 나머지 전화번호는 접두어가 될 수 없기 때문이다.


def solution(phone_book):
    phone_book.sort() # 알파벳 순으로 정렬

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]): # 앞과 뒤만 비교하여 접두사가 되는지 확인
            return False

    return True