# https://school.programmers.co.kr/learn/courses/30/lessons/12901
# Solution 1
# Python

# 요일은 7씩 반복 : 7로 나웠을 때의 나머지를 이용
# 매달 날짜는 다르므로 각각 배열에 저장

def solution(a, b) :
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]
    return day[(sum(mon[:a-1])+b) %7]

print(solution(5,24))
print(solution(7,18))
print(solution(11,20))