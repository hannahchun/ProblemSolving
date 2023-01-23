# https://school.programmers.co.kr/learn/courses/30/lessons/12943
# Solution 1
# Python

def solution(num) :
    res = num
    cnt = 0
    while(res != 1 and cnt < 500) :
        if res % 2 == 0 :
            res = res/2
        else :
            res = res*3+1
        cnt += 1
    
    if res == 1 :
        return cnt
    else :
        return -1

print(solution(6))
print(solution(16))
print(solution(626331))
