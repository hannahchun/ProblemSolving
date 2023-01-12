# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# Solution 1
# Python

def solution(number, k):
    x=[] # a stack to store the values

    # use this stack to find out the best possible largest number when k elements are removed
    for i in number :
        while x and x[-1] < i and k > 0 :
            x.pop()
            k-=1
        x.append(i)
    
    # if k is not zero, remove k items from the top of the stack
    while k > 0 :
        x.pop()
        k -=1
    
    answer = "".join(x)
    return answer

print(solution("1924",2))
print(solution("1231234",3))
print(solution("4177252841",4))
print(solution("76543",3))